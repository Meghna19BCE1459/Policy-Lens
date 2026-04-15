import os
import sys
import time
from dotenv import load_dotenv
from groq import Groq
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.append(os.path.join(os.path.abspath('.'), 'data', 'legaldocs'))
from compliance_rules import ALL_RULES

# Load API key
load_dotenv()
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def read_tos_file(filepath):
    """Read a ToS document from a text file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def chunk_text(text, chunk_size=8000):
    """Split long text into larger chunks — fewer API calls."""
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        current_length += len(word) + 1
        current_chunk.append(word)
        if current_length >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def analyze_chunk(chunk, rule):
    """Check a single rule against a single chunk."""
    prompt = f"""
You are a legal compliance expert specializing in GDPR, EU AI Act, CCPA, COPPA, DSA, and US AI policy.

Analyze the following Terms of Service excerpt and determine if it violates or conflicts with this legal requirement:

LEGAL RULE: {rule['article']}
REQUIREMENT: {rule['requirement']}

TERMS OF SERVICE EXCERPT:
{chunk}

Respond in this exact format:
VIOLATION: [YES / NO / UNCLEAR]
SEVERITY: [HIGH / MEDIUM / LOW / NONE]
EXPLANATION: [One clear sentence explaining why this is or isn't a violation]
PROBLEMATIC CLAUSE: [Quote the exact phrase from the ToS that is problematic, or write NONE]

Be strict and precise. Only flag real conflicts, not vague possibilities.
"""
    max_retries = 5
    for attempt in range(max_retries):
        try:
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            if "503" in str(e) or "UNAVAILABLE" in str(e):
                wait = 10 * (attempt + 1)
                print(f"    ⚠️ Server busy, retrying in {wait}s... (attempt {attempt+1}/{max_retries})")
                time.sleep(wait)
            elif "429" in str(e) or "rate" in str(e).lower():
                print(f"    ⚠️ Rate limit hit, waiting 30s...")
                time.sleep(30)
            else:
                print(f"    ⚠️ Error: {str(e)}")
                raise e
    return "VIOLATION: UNCLEAR\nSEVERITY: NONE\nEXPLANATION: Could not analyze due to server errors.\nPROBLEMATIC CLAUSE: NONE"

def analyze_chunk_batch(chunk, rules):
    """Check ALL rules against one chunk in a single API call."""
    rules_text = "\n".join([
        f"{i+1}. [{rule['id']}] {rule['article']}: {rule['requirement']}"
        for i, rule in enumerate(rules)
    ])

    prompt = f"""You are a legal compliance expert. Analyze this Terms of Service excerpt against each legal rule below.

TERMS OF SERVICE EXCERPT:
{chunk}

LEGAL RULES TO CHECK:
{rules_text}

For each rule, respond in this EXACT format (one per line, no extra text):
RULE_ID | VIOLATION | SEVERITY | EXPLANATION | PROBLEMATIC_CLAUSE

Where:
- RULE_ID: the rule ID e.g. GDPR-Art-5
- VIOLATION: YES, NO, or UNCLEAR
- SEVERITY: HIGH, MEDIUM, LOW, or NONE
- EXPLANATION: one sentence
- PROBLEMATIC_CLAUSE: exact quote from ToS or NONE

Only output the results, one line per rule, nothing else."""

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = groq_client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            wait = 5 * (attempt + 1)
            print(f"    ⚠️ Error: {str(e)}")
            print(f"    Retrying in {wait}s...")
            time.sleep(wait)
    return ""

def parse_response(response_text):
    """Parse a single-rule response into structured data."""
    result = {
        "violation": "NO",
        "severity": "NONE",
        "explanation": "",
        "problematic_clause": "NONE"
    }
    for line in response_text.strip().split("\n"):
        if line.startswith("VIOLATION:"):
            result["violation"] = line.replace("VIOLATION:", "").strip()
        elif line.startswith("SEVERITY:"):
            result["severity"] = line.replace("SEVERITY:", "").strip()
        elif line.startswith("EXPLANATION:"):
            result["explanation"] = line.replace("EXPLANATION:", "").strip()
        elif line.startswith("PROBLEMATIC CLAUSE:"):
            result["problematic_clause"] = line.replace("PROBLEMATIC CLAUSE:", "").strip()
    return result

def parse_batch_response(response_text, rules):
    """Parse the batched response into individual findings."""
    findings = []
    lines = response_text.strip().split("\n")

    for line in lines:
        line = line.strip()
        if "|" not in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 5:
            continue
        rule_id, violation, severity, explanation, clause = parts[0], parts[1], parts[2], parts[3], parts[4]

        if violation in ["YES", "UNCLEAR"]:
            matched = next((r for r in rules if r['id'] in rule_id), None)
            if matched:
                findings.append({
                    "rule_id": matched["id"],
                    "article": matched["article"],
                    "violation": violation,
                    "severity": severity,
                    "explanation": explanation,
                    "problematic_clause": clause
                })
    return findings

def analyze_rule(rule, chunks):
    """Check a single rule against all chunks — used for parallel execution."""
    for chunk in chunks:
        raw_response = analyze_chunk(chunk, rule)
        parsed = parse_response(raw_response)
        if parsed["violation"] in ["YES", "UNCLEAR"]:
            return {
                "rule_id": rule["id"],
                "article": rule["article"],
                "violation": parsed["violation"],
                "severity": parsed["severity"],
                "explanation": parsed["explanation"],
                "problematic_clause": parsed["problematic_clause"]
            }
    return None

def analyze_tos(filepath):
    """Full analysis pipeline — batched for speed."""
    print(f"\n📄 Reading ToS document: {filepath}")
    tos_text = read_tos_file(filepath)
    chunks = chunk_text(tos_text)
    print(f"✅ Split into {len(chunks)} chunks")
    print(f"🔍 Checking {len(ALL_RULES)} rules in {len(chunks)} batched calls...\n")

    all_findings = {}

    for i, chunk in enumerate(chunks):
        print(f"  Processing chunk {i+1}/{len(chunks)}...")
        raw = analyze_chunk_batch(chunk, ALL_RULES)
        findings = parse_batch_response(raw, ALL_RULES)
        for f in findings:
            if f["rule_id"] not in all_findings:
                all_findings[f["rule_id"]] = f

    print(f"\n✅ Done! Found {len(all_findings)} violations.")
    return list(all_findings.values())

def save_report(findings, tos_name):
    """Save the compliance report as a JSON file in outputs/."""
    import json
    from datetime import datetime

    report = {
        "document_analyzed": tos_name,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_flags": len(findings),
        "high_severity": len([f for f in findings if f["severity"] == "HIGH"]),
        "medium_severity": len([f for f in findings if f["severity"] == "MEDIUM"]),
        "findings": findings
    }

    filename = f"outputs/{tos_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print(f"\n💾 Report saved to: {filename}")

def print_report(findings, tos_name):
    """Print a clean report to the terminal."""
    print("\n" + "="*60)
    print(f"  COMPLIANCE REPORT: {tos_name}")
    print("="*60)

    if not findings:
        print("✅ No violations found!")
        return

    high = [f for f in findings if f["severity"] == "HIGH"]
    medium = [f for f in findings if f["severity"] == "MEDIUM"]
    unclear = [f for f in findings if f["violation"] == "UNCLEAR"]

    print(f"\n🔴 HIGH severity violations: {len(high)}")
    print(f"🟡 MEDIUM severity violations: {len(medium)}")
    print(f"⚪ UNCLEAR / needs review: {len(unclear)}")
    print(f"\n📊 Total flags: {len(findings)}")
    print("\n" + "-"*60)

    for i, f in enumerate(findings, 1):
        icon = "🔴" if f["severity"] == "HIGH" else "🟡" if f["severity"] == "MEDIUM" else "⚪"
        print(f"\n{icon} [{i}] {f['article']}")
        print(f"   Rule ID   : {f['rule_id']}")
        print(f"   Status    : {f['violation']}")
        print(f"   Severity  : {f['severity']}")
        print(f"   Why       : {f['explanation']}")
        print(f"   Clause    : {f['problematic_clause']}")
        print("-"*60)

if __name__ == "__main__":
    tos_path = os.path.join("data", "tosdocs", "openai_tos.txt")
    findings = analyze_tos(tos_path)
    print_report(findings, "OpenAI Terms of Service")
    save_report(findings, "OpenAI Terms of Service")
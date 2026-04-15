import streamlit as st
import os
import sys
import json
from datetime import datetime

sys.path.append(os.path.join(os.path.abspath('.'), 'data', 'legaldocs'))
from compliance_rules import ALL_RULES
from analyzer import parse_response, parse_batch_response, chunk_text, analyze_chunk_batch

# Page config
st.set_page_config(
    page_title="ToS Compliance Checker",
    page_icon="⚖️",
    layout="wide"
)

# Header
st.title("🔍 Policy Lens - Policy Compliance Checker for AI Tools")
st.markdown("Analyzes and flags GDPR, EU AI Act, CCPA, COPPA, DSA & US AI EO violations in AI product Terms of Service and Policies.")
st.divider()

# Sidebar
with st.sidebar:
    st.header("📋 About This Tool")
    st.markdown("""
    This tool analyzes Terms of Service documents and flags clauses that conflict with:
    - 🇪🇺 **GDPR** (13 articles)
    - 🤖 **EU AI Act** (9 articles)
    - 🇺🇸 **CCPA** (4 articles)
    - 👶 **COPPA** (3 articles)
    - 🌐 **DSA** (4 articles)
    - 🏛️ **US AI Executive Order** (3 articles)

    Built with **Llama 3.3 70B** via Groq API.
    """)
    st.divider()

    st.header("📚 Articles Referenced")

    st.markdown("**🇪🇺 GDPR**")
    for rule in [r for r in ALL_RULES if r['id'].startswith('GDPR')]:
        st.markdown(f"- `{rule['id']}` — {rule['article']}")

    st.divider()

    st.markdown("**🤖 EU AI Act**")
    for rule in [r for r in ALL_RULES if r['id'].startswith('EUAIA')]:
        st.markdown(f"- `{rule['id']}` — {rule['article']}")

    st.divider()

    st.markdown("**🇺🇸 CCPA**")
    for rule in [r for r in ALL_RULES if r['id'].startswith('CCPA')]:
        st.markdown(f"- `{rule['id']}` — {rule['article']}")

    st.divider()

    st.markdown("**👶 COPPA**")
    for rule in [r for r in ALL_RULES if r['id'].startswith('COPPA')]:
        st.markdown(f"- `{rule['id']}` — {rule['article']}")

    st.divider()

    st.markdown("**🌐 DSA**")
    for rule in [r for r in ALL_RULES if r['id'].startswith('DSA')]:
        st.markdown(f"- `{rule['id']}` — {rule['article']}")

    st.divider()

    st.markdown("**🏛️ US AI Executive Order**")
    for rule in [r for r in ALL_RULES if r['id'].startswith('AI-EO')]:
        st.markdown(f"- `{rule['id']}` — {rule['article']}")

    st.divider()
    gdpr_count = len([r for r in ALL_RULES if r['id'].startswith('GDPR')])
    euai_count = len([r for r in ALL_RULES if r['id'].startswith('EUAIA')])
    ccpa_count = len([r for r in ALL_RULES if r['id'].startswith('CCPA')])
    coppa_count = len([r for r in ALL_RULES if r['id'].startswith('COPPA')])
    dsa_count = len([r for r in ALL_RULES if r['id'].startswith('DSA')])
    aeo_count = len([r for r in ALL_RULES if r['id'].startswith('AI-EO')])
    st.caption(f"{len(ALL_RULES)} rules total · {gdpr_count} GDPR · {euai_count} EU AI Act · {ccpa_count} CCPA · {coppa_count} COPPA · {dsa_count} DSA · {aeo_count} AI EO")

# Input
st.subheader("📄 Input")
input_method = st.radio(
    "Choose input method:",
    ["Upload a .txt file", "Paste text directly", "Use sample (OpenAI ToS)"],
    horizontal=True
)

tos_text = ""
tos_name = ""

if input_method == "Upload a .txt file":
    uploaded_file = st.file_uploader("Upload ToS document (.txt)", type=["txt"])
    if uploaded_file:
        tos_text = uploaded_file.read().decode("utf-8")
        tos_name = uploaded_file.name.replace(".txt", "")
        st.success(f"✅ Loaded: {uploaded_file.name} ({len(tos_text.split())} words)")

elif input_method == "Paste text directly":
    tos_name = st.text_input("Document name (e.g. Google ToS)", value="Custom ToS")
    tos_text = st.text_area("Paste Terms of Service text here:", height=300)
    if tos_text:
        st.success(f"✅ {len(tos_text.split())} words loaded")

elif input_method == "Use sample (OpenAI ToS)":
    sample_path = os.path.join("data", "tosdocs", "openai_tos.txt")
    if os.path.exists(sample_path):
        with open(sample_path, "r", encoding="utf-8") as f:
            tos_text = f.read()
        tos_name = "OpenAI Terms of Service"
        st.success(f"✅ Sample loaded: OpenAI ToS ({len(tos_text.split())} words)")
    else:
        st.error("Sample file not found.")

st.divider()

# Analyze button
if tos_text:
    if st.button("🔍 Run Compliance Check", type="primary", use_container_width=True):
        progress = st.progress(0, text="Starting analysis...")
        status = st.empty()
        chunks = chunk_text(tos_text)
        all_findings = {}

        for i, chunk in enumerate(chunks):
            status.markdown(f"🔍 Processing chunk {i+1} of {len(chunks)}...")
            raw = analyze_chunk_batch(chunk, ALL_RULES)
            batch_findings = parse_batch_response(raw, ALL_RULES)
            for f in batch_findings:
                if f["rule_id"] not in all_findings:
                    all_findings[f["rule_id"]] = f
            progress.progress((i + 1) / len(chunks),
                              text=f"Processed {i+1}/{len(chunks)} chunks...")

        status.empty()
        progress.empty()

        st.session_state["findings"] = list(all_findings.values())
        st.session_state["tos_name"] = tos_name
        st.session_state["run_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Display results
if "findings" in st.session_state and st.session_state["findings"] is not None:
    findings = st.session_state["findings"]
    tos_name = st.session_state["tos_name"]
    run_date = st.session_state.get("run_date", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    high   = [f for f in findings if f["severity"] == "HIGH"]
    medium = [f for f in findings if f["severity"] == "MEDIUM"]
    low    = [f for f in findings if f["severity"] == "LOW"]

    st.subheader(f"📊 Compliance Report: {tos_name}")
    st.caption(f"Generated: {run_date}")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("🔴 High Severity", len(high))
    m2.metric("🟡 Medium Severity", len(medium))
    m3.metric("🟢 Low Severity", len(low))
    m4.metric("📊 Total Flags", len(findings))

    st.divider()

    if not findings:
        st.success("✅ No violations found!")
    else:
        sections = [
            ("🇪🇺 GDPR Violations", "GDPR"),
            ("🤖 EU AI Act Violations", "EUAIA"),
            ("🇺🇸 CCPA Violations", "CCPA"),
            ("👶 COPPA Violations", "COPPA"),
            ("🌐 DSA Violations", "DSA"),
            ("🏛️ US AI Executive Order Violations", "AI-EO"),
        ]

        for section_title, prefix in sections:
            section_findings = [f for f in findings if f["rule_id"].startswith(prefix)]
            if section_findings:
                st.markdown(f"#### {section_title}")
                for f in section_findings:
                    icon = "🔴" if f["severity"] == "HIGH" else "🟡" if f["severity"] == "MEDIUM" else "🟢"
                    with st.expander(f"{icon} `{f['rule_id']}` — {f['article']} ({f['severity']})"):
                        st.markdown(f"**Why it's a violation:** {f['explanation']}")
                        if f["problematic_clause"] and f["problematic_clause"] != "NONE":
                            st.markdown("**Problematic clause:**")
                            st.warning(f'"{f["problematic_clause"]}"')

        st.divider()
        report_data = {
            "document": tos_name,
            "date": run_date,
            "total_flags": len(findings),
            "high_severity": len(high),
            "medium_severity": len(medium),
            "low_severity": len(low),
            "findings": findings
        }
        st.download_button(
            label="⬇️ Download Report as JSON",
            data=json.dumps(report_data, indent=2),
            file_name=f"{tos_name.replace(' ', '_')}_compliance_report.json",
            mime="application/json",
            use_container_width=True
        )
else:
    st.info("👆 Load a document above and click **Run Compliance Check** to begin.")
GDPR_RULES = [
    {
        "id": "GDPR-Art-5",
        "article": "Article 5 - Principles of Data Processing",
        "requirement": "Personal data must be processed lawfully, fairly, and transparently. Data must be collected for specified, explicit, and legitimate purposes and not further processed in a manner incompatible with those purposes.",
        "keywords": ["data collection", "personal data", "processing", "purpose", "lawful"]
    },
    {
        "id": "GDPR-Art-6",
        "article": "Article 6 - Lawfulness of Processing",
        "requirement": "Processing is only lawful if the data subject has given consent, or processing is necessary for a contract, legal obligation, vital interests, public task, or legitimate interests.",
        "keywords": ["consent", "lawful basis", "legitimate interest", "contract"]
    },
    {
        "id": "GDPR-Art-7",
        "article": "Article 7 - Conditions for Consent",
        "requirement": "Consent must be freely given, specific, informed, and unambiguous. The data subject must be able to withdraw consent at any time and withdrawal must be as easy as giving consent.",
        "keywords": ["consent", "withdraw", "opt-out", "freely given", "unambiguous"]
    },
    {
        "id": "GDPR-Art-13",
        "article": "Article 13 - Information to be Provided",
        "requirement": "When collecting personal data, the controller must provide identity and contact details, purposes and legal basis for processing, recipients of data, and retention periods.",
        "keywords": ["data collection", "inform", "notify", "retention", "recipients", "third party"]
    },
    {
        "id": "GDPR-Art-17",
        "article": "Article 17 - Right to Erasure",
        "requirement": "Data subjects have the right to obtain erasure of personal data without undue delay when data is no longer necessary, consent is withdrawn, or data has been unlawfully processed.",
        "keywords": ["delete", "erasure", "right to be forgotten", "remove data", "retention"]
    },
    {
        "id": "GDPR-Art-20",
        "article": "Article 20 - Right to Data Portability",
        "requirement": "Data subjects have the right to receive their personal data in a structured, commonly used, machine-readable format and to transmit it to another controller.",
        "keywords": ["data portability", "export data", "transfer data", "machine-readable"]
    },
    {
        "id": "GDPR-Art-22",
        "article": "Article 22 - Automated Decision Making",
        "requirement": "Data subjects have the right not to be subject to solely automated decision-making, including profiling, which produces legal or similarly significant effects.",
        "keywords": ["automated decision", "profiling", "automated processing", "significant effects"]
    },
    {
        "id": "GDPR-Art-25",
        "article": "Article 25 - Data Protection by Design",
        "requirement": "Controllers must implement data protection principles and safeguards into processing activities by design and by default, ensuring minimal data collection.",
        "keywords": ["privacy by design", "data minimization", "default settings", "safeguards"]
    },
    {
        "id": "GDPR-Art-32",
        "article": "Article 32 - Security of Processing",
        "requirement": "Controllers must implement appropriate technical and organizational measures to ensure security of personal data, including encryption and pseudonymization.",
        "keywords": ["security", "encryption", "pseudonymization", "data breach", "technical measures"]
    },
    {
        "id": "GDPR-Art-33",
        "article": "Article 33 - Breach Notification",
        "requirement": "In the event of a personal data breach, the controller must notify the supervisory authority within 72 hours and communicate the breach to affected data subjects without undue delay.",
        "keywords": ["data breach", "breach notification", "72 hours", "supervisory authority", "incident"]
    },
    {
        "id": "GDPR-Art-35",
        "article": "Article 35 - Data Protection Impact Assessment",
        "requirement": "Where processing is likely to result in high risk to individuals, the controller must carry out a Data Protection Impact Assessment (DPIA) prior to processing.",
        "keywords": ["DPIA", "impact assessment", "high risk", "risk assessment", "data protection"]
    },
    {
        "id": "GDPR-Art-37",
        "article": "Article 37 - Data Protection Officer",
        "requirement": "Controllers must designate a Data Protection Officer (DPO) where processing is carried out by a public authority, involves large-scale systematic monitoring, or involves special categories of data.",
        "keywords": ["DPO", "data protection officer", "systematic monitoring", "large scale", "special categories"]
    },
    {
        "id": "GDPR-Art-44",
        "article": "Article 44 - Transfers to Third Countries",
        "requirement": "Personal data may only be transferred to third countries if adequate protection is ensured, such as through adequacy decisions or standard contractual clauses.",
        "keywords": ["third country", "international transfer", "data transfer", "adequacy", "standard contractual clauses"]
    },
]

EU_AI_ACT_RULES = [
    {
        "id": "EUAIA-Art-6",
        "article": "Article 6 - High-Risk AI Classification",
        "requirement": "AI systems used in critical infrastructure, education, employment, essential services, law enforcement, migration, or justice must be classified as high-risk and comply with strict obligations.",
        "keywords": ["high-risk", "critical infrastructure", "education", "employment", "law enforcement", "classification"]
    },
    {
        "id": "EUAIA-Art-9",
        "article": "Article 9 - Risk Management System",
        "requirement": "Providers of high-risk AI systems must establish, implement, document, and maintain a risk management system throughout the AI system lifecycle.",
        "keywords": ["risk management", "risk assessment", "high-risk AI", "lifecycle", "documentation"]
    },
    {
        "id": "EUAIA-Art-10",
        "article": "Article 10 - Training Data",
        "requirement": "High-risk AI systems must use training data that meets quality criteria, is relevant, representative, and free of errors. Data governance practices must be in place.",
        "keywords": ["training data", "data quality", "bias", "representative", "data governance"]
    },
    {
        "id": "EUAIA-Art-11",
        "article": "Article 11 - Technical Documentation",
        "requirement": "Providers of high-risk AI systems must draw up technical documentation before placing the system on the market, demonstrating compliance and enabling conformity assessment.",
        "keywords": ["technical documentation", "conformity assessment", "compliance documentation", "market placement"]
    },
    {
        "id": "EUAIA-Art-13",
        "article": "Article 13 - Transparency and Information",
        "requirement": "High-risk AI systems must be transparent and provide sufficient information for users to interpret the system's output and use it appropriately.",
        "keywords": ["transparency", "explainability", "interpretability", "AI output", "information"]
    },
    {
        "id": "EUAIA-Art-14",
        "article": "Article 14 - Human Oversight",
        "requirement": "High-risk AI systems must be designed to allow effective human oversight, including the ability to intervene, override, or stop the system.",
        "keywords": ["human oversight", "human control", "override", "intervene", "stop system"]
    },
    {
        "id": "EUAIA-Art-15",
        "article": "Article 15 - Accuracy and Robustness",
        "requirement": "High-risk AI systems must achieve appropriate levels of accuracy, robustness, and cybersecurity, and must perform consistently throughout their lifecycle.",
        "keywords": ["accuracy", "robustness", "cybersecurity", "performance", "reliability", "consistency"]
    },
    {
        "id": "EUAIA-Art-52",
        "article": "Article 52 - Transparency for Certain AI Systems",
        "requirement": "Providers of AI systems that interact with humans must ensure users are informed they are interacting with an AI, unless it is obvious from context.",
        "keywords": ["AI disclosure", "chatbot", "synthetic content", "deepfake", "inform users", "AI interaction"]
    },
    {
        "id": "EUAIA-Art-71",
        "article": "Article 71 - Prohibited AI Practices",
        "requirement": "AI systems that deploy subliminal techniques, exploit vulnerabilities, or enable social scoring by public authorities are strictly prohibited.",
        "keywords": ["prohibited", "manipulation", "subliminal", "social scoring", "exploit", "vulnerable users"]
    },
]

CCPA_RULES = [
    {
        "id": "CCPA-Sec-1798-100",
        "article": "Section 1798.100 - Right to Know",
        "requirement": "California consumers have the right to know what personal information is collected, used, shared, or sold, and businesses must disclose this upon request.",
        "keywords": ["right to know", "personal information", "disclose", "collected", "sold", "shared"]
    },
    {
        "id": "CCPA-Sec-1798-105",
        "article": "Section 1798.105 - Right to Delete",
        "requirement": "California consumers have the right to request deletion of personal information collected by a business, and the business must comply unless an exception applies.",
        "keywords": ["delete", "right to delete", "removal", "personal information", "request"]
    },
    {
        "id": "CCPA-Sec-1798-120",
        "article": "Section 1798.120 - Right to Opt-Out of Sale",
        "requirement": "California consumers have the right to opt-out of the sale of their personal information at any time. Businesses must provide a clear 'Do Not Sell My Personal Information' link.",
        "keywords": ["opt-out", "do not sell", "sale of data", "personal information", "third party sale"]
    },
    {
        "id": "CCPA-Sec-1798-125",
        "article": "Section 1798.125 - Non-Discrimination",
        "requirement": "Businesses must not discriminate against consumers who exercise their CCPA rights, including by denying goods or services, charging different prices, or providing different quality of service.",
        "keywords": ["discrimination", "equal service", "pricing", "retaliation", "consumer rights"]
    },
]

COPPA_RULES = [
    {
        "id": "COPPA-Sec-312-2",
        "article": "Section 312.2 - Definition and Scope",
        "requirement": "COPPA applies to operators of websites or online services directed to children under 13, or operators with actual knowledge they are collecting personal information from children under 13.",
        "keywords": ["children", "under 13", "minors", "child-directed", "parental consent"]
    },
    {
        "id": "COPPA-Sec-312-4",
        "article": "Section 312.4 - Notice Requirements",
        "requirement": "Operators must provide clear notice of their information practices before collecting personal information from children, including what is collected, how it is used, and disclosure practices.",
        "keywords": ["children privacy", "notice", "parental", "under 13", "disclosure", "collection"]
    },
    {
        "id": "COPPA-Sec-312-5",
        "article": "Section 312.5 - Parental Consent",
        "requirement": "Operators must obtain verifiable parental consent before collecting, using, or disclosing personal information from children under 13.",
        "keywords": ["parental consent", "verifiable consent", "children", "under 13", "guardian"]
    },
]

DSA_RULES = [
    {
        "id": "DSA-Art-14",
        "article": "Article 14 - Notice and Action Mechanisms",
        "requirement": "Online platforms must provide mechanisms for users to flag illegal content, and must process such notices in a timely, diligent, and non-arbitrary manner.",
        "keywords": ["illegal content", "notice", "flag", "reporting mechanism", "content moderation"]
    },
    {
        "id": "DSA-Art-26",
        "article": "Article 26 - Transparency of Advertising",
        "requirement": "Platforms must ensure users can identify advertisements, who paid for them, and why they were targeted. Targeting based on sensitive data is prohibited.",
        "keywords": ["advertising", "transparency", "targeted ads", "sensitive data", "political ads"]
    },
    {
        "id": "DSA-Art-27",
        "article": "Article 27 - Recommender System Transparency",
        "requirement": "Very large online platforms must provide at least one recommendation option not based on profiling, and must clearly explain the parameters used in their recommender systems.",
        "keywords": ["recommender system", "algorithm", "profiling", "transparency", "recommendation"]
    },
    {
        "id": "DSA-Art-34",
        "article": "Article 34 - Systemic Risk Assessment",
        "requirement": "Very large online platforms must assess systemic risks arising from their services, including risks to fundamental rights, public security, and electoral processes.",
        "keywords": ["systemic risk", "fundamental rights", "public security", "electoral", "risk assessment"]
    },
]

AI_EO_RULES = [
    {
        "id": "AI-EO-Sec-4-1",
        "article": "Section 4.1 - Safety and Security Standards",
        "requirement": "Developers of powerful AI systems must share safety test results with the US government before public deployment, and must notify the government of any serious risks discovered.",
        "keywords": ["safety testing", "red team", "security evaluation", "government reporting", "risk notification"]
    },
    {
        "id": "AI-EO-Sec-4-2",
        "article": "Section 4.2 - Content Authentication",
        "requirement": "AI-generated content must be clearly labeled and watermarked where technically feasible, to help users distinguish AI-generated from human-created content.",
        "keywords": ["watermark", "AI-generated content", "labeling", "synthetic media", "content authentication"]
    },
    {
        "id": "AI-EO-Sec-4-3",
        "article": "Section 4.3 - Privacy Protection",
        "requirement": "AI systems must incorporate privacy-preserving techniques and agencies must evaluate how AI collects and uses commercially available data containing personal information.",
        "keywords": ["privacy", "personal data", "privacy-preserving", "commercial data", "surveillance"]
    },
]

ALL_RULES = GDPR_RULES + EU_AI_ACT_RULES + CCPA_RULES + COPPA_RULES + DSA_RULES + AI_EO_RULES
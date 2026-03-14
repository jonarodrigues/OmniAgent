# 🛡️ OmniAgent
### *Privacy-First FinTech AI Assistant*

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Industry](https://img.shields.io/badge/Industry-FinTech-gold.svg)]()
[![Security](https://img.shields.io/badge/Security-Data%20Masking-red.svg)]()

**OmniAgent** is a sophisticated AI assistant tailored for the financial services industry. Built with a "Privacy-First" mindset, it ensures that sensitive user data (like credit card numbers or personal IDs) is masked before being processed by Large Language Models, making it ideal for integration into high-security mobile banking apps.

## 🌟 Key Features
- **Intelligent PII Masking**: Automatically detects and redacts Personally Identifiable Information (PII) before LLM submission.
- **Financial Insight Engine**: Extracts spending patterns and budgeting advice from raw transaction descriptions.
- **Mobile-Optimized Payloads**: Lean JSON structures designed for low-latency mobile performance.
- **Compliance Ready**: Built with data sovereignty and financial regulations (like LGPD/GDPR) in mind.
- **Agentic Reasoning**: Uses advanced chain-of-thought prompting to provide accurate financial recommendations.

## 🏗️ Architecture
`mermaid
graph LR
    A[User Transaction Data] --> B{Privacy Layer}
    B -->|Redacted Data| C[AI Reasoning Engine]
    C --> D[Financial Insights]
    D --> E[Mobile UI Response]
`

## 🚀 Quick Start
1. **Clone the Repo**
   `ash
   git clone https://github.com/jonarodrigues/OmniAgent.git
   cd OmniAgent
   `

2. **Install Dependencies**
   `ash
   pip install -r requirements.txt
   `

3. **Configure API Keys**
   `env
   OPENAI_API_KEY=your_key_here
   `

4. **Run Sample Analysis**
   `ash
   python main.py
   `

---

## 🔒 Security Focus
OmniAgent is designed to solve the "Trust Gap" in AI. By implementing a local redaction layer, companies can leverage the power of cloud LLMs without compromising their customers' most sensitive data.

## 🧑‍💻 About the Author
**Jonathan Rodrigues** is a Mobile Software Engineer at **PicPay**. He combines his deep expertise in mobile ecosystems with a passion for secure, intelligent AI integration in the financial sector.

---
*Empowering financial freedom with secure intelligence.*
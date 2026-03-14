import os
from loguru import logger
from dotenv import load_dotenv
from omniagent.privacy import PrivacyMasker
from omniagent.analyzer import FinanceAnalyzer

load_dotenv()

def main():
    print("--- OmniAgent: Secure FinTech AI Demo ---")
    
    # 1. Sensitive User Data (Simulation)
    raw_data = \"\"\"
    User: jonathan.rodrigues@email.com
    Transaction 1: Bought coffee for R$ 15.00 using card 1234 5678 9012 3456.
    Transaction 2: Sent PIX to 123.456.789-00 for Rent R$ 2500.00.
    Transaction 3: Salary received from PicPay R$ 8000.00.
    \"\"\"

    print(f"📄 RAW DATA (Local):\n{raw_data}")

    # 2. Masking (Local Layer)
    masker = PrivacyMasker()
    masked_data = masker.mask(raw_data)
    
    print(f"\n🛡️ MASKED DATA (Ready for LLM):\n{masked_data}")

    # 3. AI Analysis (Simulated)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("\n⚠️ Skipping AI Analysis: OPENAI_API_KEY not found in .env.")
        print("OmniAgent successfully demonstrated the Privacy Layer.")
        return

    print("\n🧠 Processing with AI Engine...")
    analyzer = FinanceAnalyzer(api_key=api_key)
    insights = analyzer.generate_insights(masked_data)
    
    print(f"\n✅ AI FINANCIAL INSIGHTS:\n{insights}")

if __name__ == "__main__":
    main()
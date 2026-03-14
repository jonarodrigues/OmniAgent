import logging
from typing import List, Dict
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

class InsightResponse(BaseModel):
    summary: str
    categories: Dict[str, float]
    recommendation: str

class FinanceAnalyzer:
    def __init__(self, api_key: str):
        self.llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=api_key, temperature=0.2)

    def generate_insights(self, masked_data: str) -> InsightResponse:
        \"\"\"
        Generates financial insights from masked transaction data.
        \"\"\"
        prompt = ChatPromptTemplate.from_template(
            \"\"\"
            You are a senior financial advisor at PicPay. 
            Analyze the following redacted transaction list and provide a 
            summary, category breakdown (percentage), and a budgeting recommendation.
            
            Transactions: {data}
            
            Return the result in clear, professional English.
            \"\"\"
        )
        
        chain = prompt | self.llm
        # Note: In a real app, we'd use a Pydantic parser here for strict mobile-ready JSON.
        response = chain.invoke({"data": masked_data})
        return response.content
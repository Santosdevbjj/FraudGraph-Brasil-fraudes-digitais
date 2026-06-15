import os
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from src.agents.prompts import SYSTEM_PROMPT

class FraudGraphAgent:
    def __init__(self):
        # Utiliza gpt-4o ou gpt-3.5-turbo para menor consumo de tokens
        self.llm = ChatOpenAI(
            model="gpt-4o",
            temperature=0.2,
            api_key=os.getenv("OPENAI_API_KEY")
        )

    def analyze_fraud_pattern(self, raw_graph_data):
        """
        Recebe o retorno do Neo4j, injeta contexto e gera
        um relatório com raciocínio analítico (Reasoning).
        """
        if not raw_graph_data:
            return "Nenhum padrão anômalo detectado no grafo nas últimas varreduras."

        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=f"Dados brutos retornados pelo grafo Neo4j: {str(raw_graph_data)}")
        ]
        
        response = self.llm.invoke(messages)
        return response.content

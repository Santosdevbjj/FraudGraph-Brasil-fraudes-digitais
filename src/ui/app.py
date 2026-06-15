import streamlit as st
from dotenv import load_dotenv
import os

# Garante o carregamento das variáveis antes de instanciar os módulos
load_dotenv()

from src.services.fraud_detector import FraudDetector
from src.agents.graph_agent import FraudGraphAgent

st.set_page_config(page_title="FraudGraph Brasil", page_icon="🛡️", layout="wide")

st.title("🛡️ FraudGraph Brasil")
st.subheader("Inteligência Agentiva e Grafos no Combate a Fraudes Digitais")

st.markdown("""
Este MVP demonstra a aplicação de **Bancos de Dados em Grafos (Neo4j)** combinados com **IA Generativa (LLMs)** 
para identificar redes de fraude digital e contas laranjas de forma preditiva.
""")

col1, col2 = st.columns([1, 2])

with col1:
    st.info("💡 **Ação de Auditoria:** Clique no botão ao lado para executar a varredura de triangulação de conexões suspeitas.")
    if st.button("🚀 Executar Varredura Antifraude", type="primary"):
        with st.spinner("Consultando conexões no Neo4j Aura..."):
            detector = FraudDetector()
            raw_results = detector.detect_high_risk_patterns()
            
        if raw_results:
            st.success(f"Padrão suspeito encontrado! {len(raw_results)} vetor(es) críticos de risco.")
            st.write("### 🗄️ Dados Brutos do Grafo (Neo4j)")
            st.json(raw_results)
            
            # Segunda onda: Raciocínio com IA
            with st.spinner("Agente de IA interpretando os relacionamentos..."):
                agent = FraudGraphAgent()
                analise_ia = agent.analyze_fraud_pattern(raw_results)
                
            st.session_state['analise_ia'] = analise_ia
        else:
            st.success("Nenhuma anomalia crítica de rede foi encontrada.")

with col2:
    st.write("### 🤖 Parecer Técnico do Agente de IA (Reasoning)")
    if 'analise_ia' in st.session_state:
        st.markdown(st.session_state['analise_ia'])
    else:
        st.write("*Aguardando execução da varredura para emitir o relatório analítico.*")

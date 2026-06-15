# FraudGraph Brasil - Inteligência Agentiva e Grafos contra Fraudes Digitais

[![Neo4j](https://img.shields.io/badge/Neo4j-Aura-blue?style=flat-square&logo=neo4j)](https://neo4j.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-MVP-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)

Este projeto foi desenvolvido especialmente para o **Aura Agent Hackathon (2026)** da Neo4j. Ele demonstra como a fusão entre bancos de dados orientados a grafos e Agentes de Inteligência Artificial com capacidade de raciocínio lógico (*Reasoning*) consegue identificar e traduzir anomalias financeiras complexas que sistemas tradicionais deixam passar.

---

## 🎯 1. Problema de Negócio (Visão Meigarom Lopes)
O crescimento de fraudes cometidas por meio de engenharia social e vetores automatizados gerou um aumento expressivo no volume de contestação de transações (*chargebacks*) e perdas financeiras operacionais no ecossistema bancário nacional. O desafio crítico não está em analisar transações isoladas, mas em **identificar as redes de relacionamento** que os criminosos utilizam (como o compartilhamento de um mesmo dispositivo móvel por dezenas de CPFs distintos para alimentar contas laranjas).

## 🏢 2. Contexto & Baseline
*   **Contexto:** Criminosos operam em "centrais de fraude", alternando contas e CPFs rapidamente no mesmo hardware para pulverizar o dinheiro roubado via transferências Pix instantâneas.
*   **Baseline:** Os sistemas antifraude tradicionais utilizam bancos relacionais (SQL) baseados em regras estáticas por cliente (ex: limite de valor por transação). Para capturar fraudes de rede em tabelas relacionais, seriam necessários múltiplos cruzamentos (*JOINs* massivos), tornando a análise em tempo real computacionalmente inviável para o negócio.

## 📋 3. Premissas da Solução
*   Dados de hardware (`device_id`) e rede (`ip`) são capturados de forma confiável no momento do login no aplicativo.
*   A concentração instantânea de mais de 3 CPFs realizando movimentações financeiras no mesmo hardware para um destino inédito é assumida como um indicador de altíssimo risco (Alerta Vermelho).

## 🛠️ 4. Estratégia da Solução & Arquitetura
Desenvolvemos uma abordagem baseada em **GraphRAG (Graph-based Retrieval-Augmented Generation)** estruturada em 4 etapas:
1.  **Ingestão de Vínculos:** Modelagem de entidades conectadas no **Neo4j Aura Cloud**.
2.  **Mapeamento de Topologia Suspeita:** Escrita de consultas otimizadas em **Cypher** para capturar ciclos fechados de transações.
3.  **Camada Agentiva:** Um agente de IA (Python + LangChain + OpenAI) que consome o subgrafo anômalo.
4.  **Apresentação Executiva:** Interface web construída via **Streamlit** para tomadores de decisão em conformidade e prevenção a fraudes.

---

┌──────────────────────┐
│   Massa de Dados     │
└──────────┬───────────┘
▼
┌───────────────────────────┐
│    Neo4j Aura Cloud       │
│ (Banco de Dados em Grafo) │
└──────────┬───────────┘
▼
┌──────────────────────────────────────────────────────────┐
│                     CAMADA AGENTIVA                      │
│                                                          │
│ ┌──────────────────┐           ┌───────────────────────┐ │
│ │  Query Cypher    ├──────────►│    Agente de IA       │ │
│ │ (Triangulação)   │           │ (Raciocínio & Contexto│ │
│ └──────────────────┘           └──────────┬────────────┘ │
└───────────────────────────────────────────┼──────────────┘
▼
┌─────────────────────────┐
│  Interface Streamlit    │
│  (Parecer de Negócio)   │
└─────────────────────────┘ 


---




## 🕸️ 5. Modelo do Grafo
O modelo foca na simplicidade e na densidade de relacionamentos:
*   `(:Cliente {cpf, nome})`
*   `(:Dispositivo {device_id, ip})`
*   `(:ContaDestino {pix, banco})`

**Relacionamentos:**
*   `(:Cliente)-[:UTILIZA]->(:Dispositivo)`
*   `(:Cliente)-[:TRANSFERIU]->(:ContaDestino)`

## ⚙️ 6. Decisões Técnicas & Trade-offs (Visão Luiz Café)
*   **Por que Neo4j?** A detecção de fraudes de rede exige a busca por padrões de caminhos (*pathfinding*). No Neo4j, o custo computacional de caminhar pelos relacionamentos é constante $O(1)$, enquanto em bancos SQL relacionais o custo cresce exponencialmente a cada novo cruzamento necessário.
*   **Por que o Agente de IA com Raciocínio?** Dados de grafos puros geram saídas estruturadas (JSON). O Agente atua como a ponte entre a Engenharia de Dados e a Diretoria de Operações, transformando métricas técnicas em um relatório interpretável em linguagem natural humana.

## 📊 7. Insights de Negócio & Resultados Simulados
A execução da query de triangulação isolou um cluster onde **3 clientes distintos (João, Maria e Pedro) utilizaram o mesmo aparelho (IPHONE999) para enviar dinheiro para o mesmo destino (`fraude@pix.com`)**.
*   **Performance de Negócio:** Em produção, a automação deste gatilho com o agente reduz o tempo de resposta do time de segurança de **horas para milissegundos**, mitigando o risco de fraude residual e preservando o caixa da instituição contra multas regulatórias.

## 🚀 8. Como Executar o Projeto
1. Clone o repositório: `git clone https://github.com/Santosdevbjj/FraudGraph-Brasil-fraudes-digitais.git`
2. Instale as dependências: `pip install -r requirements.txt`
3. Configure as variáveis de ambiente no arquivo `.env` baseado no modelo `.env.example`.
4. Inicialize o dashboard: `streamlit run src/ui/app.py`

## 🧠 9. Aprendizados & Próximos Passos
*   **Aprendizado:** A modelagem orientada a grafos simplifica drasticamente a lógica de detecção, reduzindo linhas de códigos de consultas analíticas complexas para poucas linhas de declaração declarativa em Cypher.
*   **Próximos Passos:** 1. Implementar algoritmos de grafos nativos (GDS), como o *PageRank* ou *Community Detection*, para descobrir novos padrões de fraude antes mesmo do primeiro relato de sinistro; 2. Ampliar a cobertura de testes unitários da camada do agente.


---

**Autor:** Sérgio Santos — Cientista de Dados | Ambientes Críticos e Governança de Dados

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)
 








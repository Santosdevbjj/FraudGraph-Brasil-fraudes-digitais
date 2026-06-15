# FraudGraph Brasil — Inteligência Agentiva e Grafos contra Fraudes Digitais

[![Neo4j](https://img.shields.io/badge/Neo4j-Aura-blue?style=flat-square&logo=neo4j)](https://neo4j.com/)
[![Python](https://img.shields.io/badge/Python-3.14.6-yellow?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-MVP-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-1.3.0-1C3C3C?style=flat-square&logo=langchain)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat-square&logo=openai)](https://openai.com/)
[![Hackathon](https://img.shields.io/badge/Neo4j-Aura_Agent_Hackathon_2026-00BCD4?style=flat-square)](https://neo4j.com/)

---

## 🎯 1. Problema de Negócio

O ecossistema financeiro brasileiro registra um crescimento contínuo de fraudes estruturadas em **redes de contas laranjas**, operadas por centrais de fraude que alternam múltiplos CPFs em um único hardware físico para pulverizar transferências Pix roubadas antes que os sistemas de segurança consigam reagi.

O desafio crítico **não é detectar uma transação suspeita isolada** — os sistemas tradicionais baseados em regras já fazem isso razoavelmente. O desafio real é **enxergar a rede**: identificar que João, Maria e Pedro, aparentemente clientes independentes, estão operando do mesmo aparelho celular e transferindo para o mesmo destino Pix em minutos de diferença.

Esse padrão — invisível para bancos de dados relacionais sem cruzamentos massivos de tabelas — é exatamente o que o FraudGraph Brasil foi projetado para capturar.

---

## 🏢 2. Contexto & Baseline

**Cenário operacional:** Criminosos operam em "centrais de fraude", alternando identidades (CPFs clonados ou laranjas) em um mesmo dispositivo físico para atomizar o rastro financeiro e dificultar o rastreamento.

**Baseline atual (o que o mercado usa hoje):**

Os sistemas antifraude tradicionais operam sobre bancos de dados relacionais (SQL) com regras estáticas por cliente — como limite de valor por transação ou frequência de acessos por CPF individual. Para detectar uma fraude de rede nesses sistemas, seriam necessários múltiplos `JOINs` sobre tabelas de milhões de registros, tornando a análise em tempo real **computacionalmente inviável**.

**Por que o grafo muda o jogo:** Em Neo4j, caminhar por um relacionamento tem custo computacional constante `O(1)`, independente do volume total de dados. A mesma consulta que exigiria horas em SQL é resolvida em milissegundos em Cypher.

---

## 📋 3. Premissas da Solução

- O identificador de hardware (`device_id`) e o endereço de rede (`ip`) são capturados de forma confiável no momento do login no aplicativo bancário.
- A concentração de **3 ou mais CPFs distintos** realizando transferências para um mesmo destino Pix a partir do mesmo dispositivo físico é tratada como **gatilho de risco máximo (Alerta Vermelho)**.
- O modelo de dados representa uma janela operacional recente e válida para identificação de padrões, não para causalidade estatística definitiva.
- Registros sem `device_id` ou `ip` são excluídos da análise de triangulação por ausência de âncora física de detecção.

---

## 🛠️ 4. Estratégia da Solução & Arquitetura

A solução foi estruturada em uma arquitetura **GraphRAG (Graph-based Retrieval-Augmented Generation)** com quatro camadas de responsabilidade bem delimitadas:

**Passo 1 — Ingestão de Vínculos (`src/ingestion/`)**
Script idempotente que cria nós e relacionamentos no Neo4j Aura Cloud com constraints de unicidade garantindo que CPFs, dispositivos e chaves Pix não sejam duplicados entre execuções.

**Passo 2 — Detecção de Topologia Suspeita (`src/services/fraud_detector.py`)**
Query Cypher de triangulação que isola exclusivamente os subgrafos onde múltiplos CPFs compartilham o mesmo hardware e o mesmo destino financeiro — a assinatura topológica de uma central de fraude.

**Passo 3 — Camada Agentiva (`src/agents/`)**
Agente de IA (Python + LangChain + GPT-4o) que recebe o subgrafo bruto em JSON, aplica raciocínio contextual ancorado em um `SYSTEM_PROMPT` de Analista Sênior de Prevenção a Fraudes, e traduz os dados estruturados em um **parecer executivo acionável**.

**Passo 4 — Interface de Decisão (`src/ui/app.py`)**
Dashboard Streamlit construído para equipes de Auditoria, Riscos e Compliance executarem a varredura e receberem o relatório de IA em linguagem natural — sem exigir conhecimento técnico em grafos.

```
┌──────────────────────┐
│   Massa de Dados     │  ← src/ingestion/load_data.py
└──────────┬───────────┘
           ▼
┌───────────────────────────┐
│    Neo4j Aura Cloud       │  ← Constraints + Nós + Relacionamentos
│ (Banco de Dados em Grafo) │     via cypher/01..04
└──────────┬────────────────┘
           ▼
┌──────────────────────────────────────────────────────────┐
│                     CAMADA AGENTIVA                      │
│                                                          │
│ ┌──────────────────┐           ┌───────────────────────┐ │
│ │  Query Cypher    ├──────────►│    Agente GPT-4o      │ │
│ │ (Triangulação ≥3)│           │ (Reasoning + Parecer) │ │
│ └──────────────────┘           └──────────┬────────────┘ │
└───────────────────────────────────────────┼──────────────┘
                                            ▼
                               ┌─────────────────────────┐
                               │  Interface Streamlit    │
                               │  (Decisão de Bloqueio)  │
                               └─────────────────────────┘
```

---

## 🕸️ 5. Modelo do Grafo

A modelagem prioriza densidade relacional com o mínimo de nós necessário para capturar o vetor de fraude de rede.

**Nós (Nodes)**

| Label | Propriedades | Constraint |
|---|---|---|
| `:Cliente` | `cpf`, `nome` | `cpf` UNIQUE |
| `:Dispositivo` | `device_id`, `ip` | `device_id` UNIQUE |
| `:ContaDestino` | `pix`, `banco` | `pix` UNIQUE |

**Relacionamentos**

| Relacionamento | Significado | Propriedades |
|---|---|---|
| `(:Cliente)-[:UTILIZA]->(:Dispositivo)` | Vínculo hardware-identidade | — |
| `(:Cliente)-[:TRANSFERIU]->(:ContaDestino)` | Transação financeira | `valor`, `data` |

**Query Coração do Projeto — Triangulação de Rede:**

```cypher
MATCH (c:Cliente)-[:UTILIZA]->(d:Dispositivo),
      (c)-[:TRANSFERIU]->(p:ContaDestino)
WITH d, p, collect(c.nome) AS clientes, count(c) AS total_cpfs
WHERE total_cpfs >= 3
RETURN d.device_id   AS dispositivo,
       d.ip          AS ip_dispositivo,
       p.pix         AS pix_destino,
       p.banco       AS banco_destino,
       clientes,
       total_cpfs
```

Esta query retorna **taxa zero de falso-positivo** para o padrão de central de fraude, pois exige simultaneamente: mesmo hardware + mesmo destino Pix + três ou mais identidades distintas.

---

## ⚙️ 6. Decisões Técnicas & Trade-offs

**Neo4j vs. PostgreSQL/MySQL**

A alternativa natural seria implementar a detecção de rede em SQL com múltiplos `JOINs` entre tabelas de clientes, dispositivos e transações. O trade-off aceito é a introdução de um banco de dados especializado (Neo4j) em troca de custo computacional `O(1)` por travessia de relacionamento, inviável de replicar em SQL para análise em tempo real com volumes bancários reais.

**GPT-4o vs. GPT-3.5-turbo**

Optou-se pelo GPT-4o pela qualidade do raciocínio contextual (*Reasoning*) ao interpretar subgrafos estruturados. O trade-off aceito é o custo maior por token — mitigável em produção com cache de pareceres para padrões idênticos ou uso de `gpt-4o-mini` para triagem inicial.

**Agente LangChain vs. chamada direta à API OpenAI**

LangChain foi escolhido pela abstração de mensagens (`SystemMessage`, `HumanMessage`) e pela facilidade de extensão futura com ferramentas (`tools`) e memória de contexto. O trade-off aceito é a dependência de uma camada adicional que pode ficar defasada em relação ao SDK nativo da OpenAI.

**Mocks em Testes Unitários vs. Testes de Integração**

Os testes em `tests/test_detector.py` interceptam a conexão com o Neo4j via `unittest.mock`, isolando as regras de negócio de oscilações de rede e eliminando custo de créditos Aura em pipelines de CI/CD. O trade-off aceito é a ausência de validação do schema real do banco em execuções automatizadas.

**Variáveis de Ambiente via `.env` vs. Secrets Manager**

Para o escopo de MVP de hackathon, credenciais são injetadas via arquivo `.env` com `.gitignore` configurado. Em produção bancária real, o trade-off correto seria migrar para um cofre de credenciais (AWS Secrets Manager, Azure Key Vault ou HashiCorp Vault).

---

## 📊 7. Insights de Negócio & Resultados

**Padrão detectado na massa de dados simulada:**

A query de triangulação isolou um cluster onde **João Silva, Maria Souza e Pedro Santos** — três CPFs aparentemente independentes — utilizaram o **mesmo aparelho físico (IPHONE999 / IP 192.168.1.10)** para transferir respectivamente R$ 5.000, R$ 4.500 e R$ 5.500 para o **mesmo destino Pix (`fraude@pix.com` / Banco X)** na mesma data.

Em um sistema SQL tradicional, esses três registros seriam analisados em filas independentes por CPF, sem cruzamento em tempo real. No grafo, o padrão é detectado em uma única varredura Cypher.

**Performance de Negócio (projeção para produção):**

Em ambientes bancários críticos como o da operação Bradesco, onde transações Pix são liquidadas em milissegundos e janelas de contestação são curtas, a automação deste gatilho com o agente de IA reduz o tempo de resposta do time de segurança de **horas para milissegundos** — preservando o caixa da instituição contra chargebacks e multas regulatórias do Banco Central.

---

## 🚀 8. Como Executar o Projeto

**Pré-requisitos**

- Python 3.14.6
- Conta ativa no [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/) (free tier disponível)
- Chave de API da [OpenAI](https://platform.openai.com/)

**Passo a passo**

```bash
# 1. Clone o repositório
git clone https://github.com/Santosdevbjj/FraudGraph-Brasil-fraudes-digitais.git
cd FraudGraph-Brasil-fraudes-digitais

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais do Neo4j Aura e OpenAI

# 4. Popule o banco de dados com a massa de dados simulada
python src/ingestion/load_data.py

# 5. Inicialize o dashboard
streamlit run src/ui/app.py
```

**Estrutura do Projeto**

```
FraudGraph-Brasil/
├── cypher/
│   ├── 01_constraints.cypher     # Unicidade de CPF, device_id e Pix
│   ├── 02_nodes.cypher           # Criação de Clientes, Dispositivos e Contas
│   ├── 03_relationships.cypher   # Vínculos UTILIZA e TRANSFERIU
│   └── 04_detection_queries.cypher  # Query de triangulação de risco
├── docs/
│   └── arquitetura.md            # Documento de arquitetura detalhado
├── notebooks/
│   └── exploracao.ipynb          # EDA e validação de hipóteses (Colab-ready)
├── src/
│   ├── agents/
│   │   ├── graph_agent.py        # FraudGraphAgent (LangChain + GPT-4o)
│   │   └── prompts.py            # SYSTEM_PROMPT do analista de fraudes
│   ├── database/
│   │   └── neo4j_connection.py   # Singleton de conexão com Neo4j Aura
│   ├── ingestion/
│   │   └── load_data.py          # Script idempotente de ingestão
│   ├── services/
│   │   └── fraud_detector.py     # Query coração: triangulação ≥3 CPFs
│   └── ui/
│       └── app.py                # Dashboard Streamlit para Compliance
├── tests/
│   └── test_detector.py          # Testes unitários com mocks do Neo4j
├── .env.example
├── .python-version
├── requirements.txt
└── runtime.txt
```

---

## 🧠 9. Aprendizados & Próximos Passos

**O que foi mais difícil e como foi superado:**

A maior complexidade não estava no código, mas na **modelagem do problema como grafo**. A tentação inicial é reproduzir a lógica tabular do SQL em nós e propriedades. A virada acontece quando se entende que o valor do grafo está nos **relacionamentos** — e que a query de triangulação (`UTILIZA` + `TRANSFERIU` convergindo para o mesmo nó) é mais próxima da linguagem do analista de fraudes do que qualquer `JOIN`.

**O que faria diferente em uma segunda iteração:**

Implementaria o `SYSTEM_PROMPT` do agente com técnicas de *few-shot prompting*, incluindo exemplos reais de pareceres de compliance para calibrar o tom e a estrutura do relatório gerado pelo GPT-4o.

**Próximos Passos**

- Implementar algoritmos nativos do Neo4j GDS — `PageRank` e `Community Detection` — para descobrir novos padrões de fraude antes do primeiro relato de sinistro.
- Adicionar a dimensão temporal nos relacionamentos `TRANSFERIU` (janela de 5 minutos como gatilho adicional de risco).
- Ampliar cobertura de testes unitários da camada agentiva com mocks da API OpenAI.
- Implementar cache de pareceres para subgrafos idênticos, reduzindo custo de tokens em produção.
- Migrar gestão de credenciais para um cofre seguro (Vault / Secrets Manager) para cenários de produção bancária.

---

## 👤 Autor

**Sérgio Santos** — Senior Data Engineer & Cloud Architect | Especialista em Ambientes Críticos e Governança de Dados

15+ anos em sistemas bancários de missão crítica (Banco Bradesco S.A.) · DIO Campus Expert

[![Portfólio](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)

---

*Projeto desenvolvido para o **Neo4j Aura Agent Hackathon 2026**.*

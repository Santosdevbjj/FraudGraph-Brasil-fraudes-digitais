# FraudGraph Brasil — Inteligência Agentiva e Grafos contra Fraudes Digitais

[![Neo4j](https://img.shields.io/badge/Neo4j-Aura-blue?style=flat-square&logo=neo4j)](https://neo4j.com/)
[![Python](https://img.shields.io/badge/Python-3.14.6-yellow?style=flat-square&logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-MVP-FF4B4B?style=flat-square&logo=streamlit)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-1.3.0-1C3C3C?style=flat-square&logo=langchain)](https://www.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat-square&logo=openai)](https://openai.com/)
[![Hackathon](https://img.shields.io/badge/Neo4j-Aura_Agent_Hackathon_2026-00BCD4?style=flat-square)](https://neo4j.com/)

---

## 📌 Resumo Executivo

**FraudGraph Brasil** é um agente inteligente de investigação de fraudes digitais baseado em **Neo4j Aura** e **Inteligência Artificial Generativa**.

A solução identifica padrões suspeitos envolvendo CPFs, dispositivos físicos compartilhados e contas de destino recorrentes — permitindo que analistas de compliance detectem possíveis esquemas fraudulentos em **segundos**, não em horas.

O projeto demonstra como bancos de dados em grafos, combinados com LLMs, eliminam o principal ponto cego dos sistemas antifraude tradicionais: a **invisibilidade das conexões entre entidades aparentemente independentes**.

> Este projeto foi inspirado em desafios reais observados ao longo de uma trajetória profissional em ambientes de processamento bancário e sistemas de missão crítica, adaptados para fins de demonstração tecnológica no contexto do Neo4j Aura Agent Hackathon 2026.

---

## 🎯 1. Problema de Negócio

Instituições financeiras brasileiras enfrentam perdas crescentes decorrentes de fraudes digitais estruturadas em **redes de contas laranjas**.

Grande parte dessas fraudes opera com múltiplos CPFs distintos, dispositivos físicos compartilhados e contas de destino recorrentes — um padrão que sistemas tradicionais **analisam em filas isoladas por cliente**, sem capacidade de cruzar esses vetores em tempo real.

O resultado é que João, Maria e Pedro — aparentemente três clientes independentes — transferem dinheiro do mesmo aparelho celular para o mesmo destino Pix em minutos de diferença, e os alertas só chegam **horas depois**, quando o dinheiro já foi pulverizado.

O desafio central não é detectar uma transação suspeita isolada. É **enxergar a rede**.

---

## 🏢 2. Contexto

Criminosos organizam "centrais de fraude" onde múltiplas identidades (CPFs clonados ou laranjas) são operadas no mesmo hardware físico para atomizar transferências Pix antes que os sistemas de segurança reajam.

**O que os sistemas atuais fazem:**
Bancos de dados relacionais (SQL) aplicam regras estáticas por CPF — limite de valor, frequência de acesso, score individual. Para capturar fraudes de rede nesse modelo, seriam necessários múltiplos `JOINs` entre tabelas de milhões de registros, tornando a análise em tempo real **computacionalmente inviável**.

**O que o grafo muda:**
Em Neo4j, caminhar por um relacionamento tem custo `O(1)`, independente do volume total de dados. A mesma detecção que exigiria minutos em SQL é resolvida em milissegundos em Cypher — tornando a análise de rede viável dentro da janela de liquidação instantânea do Pix.

---

## 📋 3. Premissas

- Um dispositivo físico (`device_id`) pode ser utilizado por múltiplos clientes — mas o compartilhamento por **3 ou mais CPFs distintos** direcionados ao mesmo destino financeiro é tratado como **indicador de risco máximo**.
- Uma conta destino pode receber recursos de múltiplos clientes — mas a recorrência coordenada a partir do mesmo hardware é a assinatura topológica de uma central de fraude.
- O identificador de hardware e o endereço IP são capturados de forma confiável no momento do login no aplicativo bancário.
- O modelo representa uma janela operacional recente válida para identificação de padrões, não para causalidade estatística definitiva.
- Registros sem `device_id` são excluídos da análise de triangulação por ausência de âncora física de detecção.

---

## 🛠️ 4. Estratégia da Solução

A solução mapeia o problema como um problema de **topologia de grafo**, não de filtragem de registros:

```
      (:Cliente {cpf})
            ↓  [:UTILIZA]
      (:Dispositivo {device_id})
            ↑  [:UTILIZA]
  (:Cliente) (:Cliente) ...

      (:Cliente)
            ↓  [:TRANSFERIU]
      (:ContaDestino {pix})
            ↑  [:TRANSFERIU]
  (:Cliente) (:Cliente) ...
```

Quando os dois padrões convergem — **mesmo dispositivo + mesmo destino + 3 ou mais CPFs** — a query Cypher de triangulação sinaliza o cluster como vetor de fraude de rede.

Essa abordagem transforma a detecção de fraude de uma operação de varredura em tabelas para uma **travessia de grafo direcionada**, respondendo em milissegundos.

---

## 🏛️ 5. Arquitetura

```
   [ Analista / Interface Web ]
              ↓
       [ Streamlit UI ]          ← src/ui/app.py
              ↓
     [ Aura Agent (IA) ]         ← src/agents/graph_agent.py
       GPT-4o + LangChain          (Reasoning + Parecer Executivo)
              ↓
      [ Neo4j Aura Cloud ]       ← src/services/fraud_detector.py
     Query Cypher O(1)             (Triangulação ≥ 3 CPFs)
              ↓
       [ Massa de Dados ]        ← src/ingestion/load_data.py
    Clientes · Dispositivos        (Ingestão Idempotente)
      Contas Destino
```

**Separação de responsabilidades:**

| Camada | Responsabilidade |
|---|---|
| `ingestion/` | Criação idempotente de nós e relacionamentos no Aura |
| `services/` | Query Cypher de triangulação — detecção pura de padrão |
| `agents/` | Interpretação do subgrafo em linguagem natural (LLM) |
| `ui/` | Interface de decisão para equipes de Compliance |
| `tests/` | Testes unitários com mocks — regras de negócio isoladas de infraestrutura |

---

## 🕸️ 6. Modelagem do Grafo

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

Esta query exige simultaneamente: mesmo hardware + mesmo destino Pix + três ou mais identidades distintas — **reduzindo significativamente a incidência de falsos positivos para este cenário de fraude.**

---

## ⚙️ 7. Decisões Técnicas & Trade-offs

**Por que Neo4j e não PostgreSQL/MySQL?**

Fraudes digitais estruturadas são fundamentalmente um **problema de relacionamento**, não de registro. Bancos relacionais armazenam eventos isolados com eficiência — mas cruzar três tabelas (clientes, dispositivos, transações) para encontrar convergências em tempo real exige `JOINs` de custo crescente. Grafos identificam conexões com custo `O(1)` por travessia. Por isso Neo4j foi escolhido.

*Trade-off aceito:* introdução de um banco especializado adicional na arquitetura, com curva de aprendizado em Cypher.

**Por que Streamlit e não FastAPI + React?**

Streamlit permite construir rapidamente uma interface funcional para demonstração do agente sem overhead de frontend separado — adequado para o escopo de MVP de hackathon.

*Trade-off aceito:* menor flexibilidade de UI em troca de velocidade de entrega e foco no diferencial real do projeto (grafo + IA).

**Por que IA Generativa (GPT-4o) e não regras fixas?**

Regras fixas produzem alertas estruturados — mas exigem que o analista interprete os dados brutos do grafo. O agente GPT-4o transforma o subgrafo JSON em **parecer executivo em linguagem natural**, tornando a decisão de bloqueio acessível para Diretores de Operações sem conhecimento técnico em grafos.

*Trade-off aceito:* custo por token e latência da chamada à API OpenAI — mitigável com cache de pareceres para padrões idênticos.

**Por que mocks nos testes unitários?**

Os testes em `tests/test_detector.py` interceptam a conexão com o Neo4j via `unittest.mock`, isolando as regras de negócio de oscilações de rede e eliminando custo de créditos Aura em pipelines de CI/CD.

*Trade-off aceito:* ausência de validação do schema real do banco em execuções automatizadas — coberta manualmente via `notebooks/exploracao.ipynb`.

---

## 🤖 8. Implementação do Agente

O agente opera em três etapas sequenciais:

**Etapa 1 — Consulta ao Grafo**
`FraudDetector.detect_high_risk_patterns()` executa a query de triangulação e retorna o subgrafo anômalo como lista de dicionários JSON.

**Etapa 2 — Injeção de Contexto**
O `SYSTEM_PROMPT` ancora o modelo GPT-4o na persona de *Analista Sênior de Prevenção a Fraudes Bancárias*, com foco em identificar o padrão técnico suspeito, explicar o risco operacional e recomendar ações imediatas de bloqueio.

**Etapa 3 — Geração do Parecer**
`FraudGraphAgent.analyze_fraud_pattern()` combina o prompt de sistema com os dados brutos do grafo e retorna um relatório em linguagem natural estruturado para tomada de decisão — sem exigir que o analista leia JSON ou entenda Cypher.

---

## 📊 9. Resultados

**Padrão detectado na massa de dados simulada:**

A query de triangulação isolou um cluster onde **João Silva, Maria Souza e Pedro Santos** — três CPFs aparentemente independentes — utilizaram o **mesmo aparelho físico (IPHONE999 / IP 192.168.1.10)** para transferir respectivamente R$ 5.000, R$ 4.500 e R$ 5.500 para o **mesmo destino Pix (`fraude@pix.com` / Banco X)** na mesma data.

Em um sistema SQL tradicional, esses três registros seriam analisados em filas independentes por CPF. No grafo, o padrão é detectado em **uma única varredura Cypher**.

---

## 💼 10. Impacto de Negócio

Em uma investigação tradicional, um analista de compliance poderia gastar vários minutos — ou horas — correlacionando transações manualmente entre planilhas e sistemas legados para identificar que três clientes distintos compartilham o mesmo hardware.

Com o FraudGraph Brasil, **padrões suspeitos são identificados em segundos** através da análise de relacionamentos em grafos, e o parecer do agente de IA entrega a recomendação de bloqueio já formatada para ação imediata.

**Impacto esperado em ambiente de produção:**

- Redução expressiva do tempo de investigação por ocorrência
- Maior visibilidade de conexões ocultas entre entidades aparentemente independentes
- Apoio à tomada de decisão por equipes sem background técnico em grafos
- Melhor priorização de alertas com base em densidade de relacionamentos suspeitos
- Redução de chargebacks e exposição a multas regulatórias do Banco Central

---

## 🧠 11. Aprendizados

O maior aprendizado deste projeto não foi técnico — foi conceitual.

A tentação inicial ao modelar o problema foi reproduzir a lógica tabular do SQL em nós e propriedades. A virada acontece quando se compreende que o **valor do grafo está nos relacionamentos**, não nos nós individuais. A query de triangulação é mais próxima da linguagem do analista de fraudes do que qualquer `JOIN` poderia ser.

Durante o desenvolvimento, os aprendizados técnicos consolidados foram:

- Modelagem orientada a relacionamentos no Neo4j Aura Cloud
- Escrita de queries Cypher para detecção de padrões de rede
- Construção de agentes baseados em grafos com LangChain e GPT-4o
- Engenharia de prompts para investigação de fraudes financeiras
- Arquitetura GraphRAG: da consulta estruturada ao parecer em linguagem natural
- Isolamento de regras de negócio em testes unitários com mocks de infraestrutura

---

## 🚀 12. Próximos Passos

- Implementar algoritmos nativos do **Neo4j GDS** — `PageRank` e `Community Detection` — para descobrir novos padrões de fraude antes do primeiro relato de sinistro
- Adicionar **dimensão temporal** nos relacionamentos `TRANSFERIU` (janela de 5 minutos como gatilho adicional de risco)
- Ampliar cobertura de testes unitários da camada agentiva com mocks da API OpenAI
- Implementar **cache de pareceres** para subgrafos idênticos, reduzindo custo de tokens em produção
- Migrar gestão de credenciais para cofre seguro (Vault / Secrets Manager) para cenários de produção bancária

---

## ▶️ 13. Como Executar o Projeto

**Pré-requisitos**

- Python 3.14.6
- Conta ativa no [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/) (free tier disponível)
- Chave de API da [OpenAI](https://platform.openai.com/)

**Passo a passo**

```bash
# Clone o repositório
git clone https://github.com/Santosdevbjj/FraudGraph-Brasil-fraudes-digitais.git
cd FraudGraph-Brasil-fraudes-digitais

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas credenciais do Neo4j Aura e OpenAI

# Popule o banco de dados com a massa de dados simulada
python src/ingestion/load_data.py

# Inicialize o dashboard
streamlit run src/ui/app.py
```

**Estrutura do Projeto**

```
FraudGraph-Brasil/
├── cypher/
│   ├── 01_constraints.cypher        # Unicidade de CPF, device_id e Pix
│   ├── 02_nodes.cypher              # Criação de Clientes, Dispositivos e Contas
│   ├── 03_relationships.cypher      # Vínculos UTILIZA e TRANSFERIU
│   └── 04_detection_queries.cypher  # Query de triangulação de risco
├── docs/
│   └── arquitetura.md               # Documento de arquitetura detalhado
├── notebooks/
│   └── exploracao.ipynb             # EDA e validação de hipóteses (Colab-ready)
├── src/
│   ├── agents/
│   │   ├── graph_agent.py           # FraudGraphAgent (LangChain + GPT-4o)
│   │   └── prompts.py               # SYSTEM_PROMPT do analista de fraudes
│   ├── database/
│   │   └── neo4j_connection.py      # Singleton de conexão com Neo4j Aura
│   ├── ingestion/
│   │   └── load_data.py             # Script idempotente de ingestão
│   ├── services/
│   │   └── fraud_detector.py        # Query coração: triangulação ≥ 3 CPFs
│   └── ui/
│       └── app.py                   # Dashboard Streamlit para Compliance
├── tests/
│   └── test_detector.py             # Testes unitários com mocks do Neo4j
├── .env.example
├── .python-version
├── requirements.txt
└── runtime.txt
```

---

## 👤 14. Autor

**Sérgio Santos** — Senior Data Engineer & Cloud Architect

15+ anos em sistemas bancários de missão crítica (Banco Bradesco S.A.) · DIO Campus Expert

[![Portfólio](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://portfoliosantossergio.vercel.app)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz)

---

*Projeto desenvolvido para o **Neo4j Aura Agent Hackathon 2026**.*

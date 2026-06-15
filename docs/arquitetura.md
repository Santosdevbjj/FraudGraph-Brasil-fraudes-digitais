# 🏛️ Documento de Arquitetura da Solução - FraudGraph Brasil

Este documento detalha as decisões de design, fluxo de dados, modelo de dados em grafos e a lógica da camada agentiva da plataforma **FraudGraph Brasil**, desenvolvida para o **Neo4j Aura Agent Hackathon**.

---

## 1. Visão Geral do Sistema

O **FraudGraph Brasil** é uma solução de prevenção a fraudes digitais e identificação de contas laranjas em transações Pix. O sistema difere das soluções tradicionais de mercado por não analisar eventos isolados, mas sim a **topologia de relacionamentos** entre entidades (Clientes, Dispositivos e Contas de Destino), utilizando **Bancos de Dados Orientados a Grafos (Neo4j)** combinados com **Modelos de Linguagem de Grande Porte (LLMs)** em uma arquitetura **GraphRAG**.

---

## 2. Fluxo de Dados e Componentes da Solução

O ecossistema foi projetado de forma modular, garantindo baixo acoplamento e separação estrita de responsabilidades:

1. **Camada de Ingestão (`src/ingestion/`):** Consome eventos brutos de acesso e movimentações financeiras, criando nós e relacionamentos de forma idempotente e aplicando restrições de integridade (*Constraints*).
2. **Camada de Dados de Relacionamento (Neo4j Aura Cloud):** Executa buscas de caminhos (*Pathfinding*) e fechamento de ciclos anômalos em tempo real com custo computacional $O(1)$.
3. **Camada de Detecção de Padrões (`src/services/`):** Isola queries Cypher de alta performance para extrair subgrafos que correspondam a vetores de risco de fraude de rede (Triangulação).
4. **Camada Agentiva de IA (`src/agents/`):** Consome a estrutura estruturada em JSON gerada pela consulta do grafo, aplica uma persona analítica de prevenção a fraudes e gera um parecer em linguagem natural contendo o raciocínio clínico do risco (*Reasoning*).
5. **Camada de Apresentação (`src/ui/`):** Dashboard analítico construído em Streamlit focado nas equipes de Auditoria, Riscos e Compliance.

---

```

[ Usuário / Dispositivo ] ──(Captura de Evento)──► [ API Streamlit ]
│
┌───────────────────────────────────────────────────────────┘
▼
[ Ingestão de Dados ] ──► [ Neo4j Aura Cloud ]
│
(Query Cypher de Rede)
│
▼
[ FraudDetector ] ──(Subgrafo Bruto)──┐
▼
[ FraudGraphAgent ]
│
(Raciocínio LLM)
│
▼
[ Parecer de Negócio ]  


```

---




## 3. Modelagem de Grafos

A modelagem prioriza a densidade relacional e a eliminação de cruzamentos (*JOINs*) custosos em tabelas relacionais.

### Nós (Nodes)
* `(:Cliente)`: Representa o correntista ou usuário da aplicação.
    * *Propriedades*: `cpf` (String, Chave Única), `nome` (String).
* `(:Dispositivo)`: Representa a assinatura física do hardware utilizado no acesso.
    * *Propriedades*: `device_id` (String, Chave Única), `ip` (String).
* `(:ContaDestino)`: Representa a ponta recebedora do fluxo financeiro.
    * *Propriedades*: `pix` (String, Chave Única), `banco` (String).

### Relacionamentos (Relationships)
* `(:Cliente)-[:UTILIZA]->(:Dispositivo)`: Mapeia o vínculo de uso entre a pessoa e o aparelho telefônico/computador.
* `(:Cliente)-[:TRANSFERIU]->(:ContaDestino)`: Representa a transação financeira direta.
    * *Propriedades*: `valor` (Float), `data` (String).

---

## 4. O Coração da Detecção: Triangulação de Rede

Sistemas tradicionais falham em detectar fraudadores que alternam múltiplas identidades (CPFs clonados) em uma mesma máquina física para espalhar dinheiro roubado rápido. A nossa consulta Cypher ataca essa vulnerabilidade mapeando a **triangulação** das entidades de risco:

```cypher
MATCH (c:Cliente)-[:UTILIZA]->(d:Dispositivo),
      (c)-[:TRANSFERIU]->(p:ContaDestino)
WITH d, p, collect(c.nome) as clientes, count(c) as total_cpfs
WHERE total_cpfs >= 3
RETURN d.device_id as dispositivo, 
       d.ip as ip_dispositivo, 
       p.pix as pix_destino, 
       p.banco as banco_destino, 
       clientes, 
       total_cpfs

```

---

Esta query atua filtrando exclusivamente os pontos onde múltiplos usuários distintos operam no mesmo identificador de hardware com destino a um mesmo elo final, fornecendo uma taxa zero de falso-positivo para identificação de "centrais de fraude" ou redes de contas laranjas.



## ​5. Raciocínio Inteligente com Agente IA (GraphRAG)

​Em vez de devolver o resultado JSON bruto para os analistas humanos, a camada agentiva (alimentada por modelos gpt-4o) realiza o processamento contextual:
​Entrada Estruturada: O agente recebe a lista de nós do subgrafo comprometido.
​Injeção de Contexto: O SYSTEM_PROMPT ancora a IA a atuar estritamente como um Diretor de Compliance Bancário Senior.


​Raciocínio Técnico (Reasoning): A IA decodifica os nós de grafos e infere o modus operandi da fraude (Ex: "Identificou-se padrão típico de Engenharia Social com pulverização coordenada de saldos no mesmo terminal móvel").


​Output Orientado a Ações: O agente recomenda ações imediatas de segurança, como bloqueio preventivo das contas de destino e bloqueio de novas autenticações a partir do device_id comprometido.


---


## ​6. Decisões de Engenharia e Trade-offs

​Neo4j Connection Singleton: A classe Neo4jConnection implementa um padrão que gerencia o ciclo de vida do Driver de conexão de forma centralizada, mitigando o vazamento de sockets e esgotamento de conexões na instância servida pelo Aura Cloud.


​Mocks em Testes Unitários: O pipeline de testes (tests/test_detector.py) intercepta chamadas de infraestrutura. Isso isola as regras de negócio de oscilações de rede externa e elimina o custo financeiro e de latência durante as esteiras automáticas de integração contínua (CI/CD).


​Arquitetura Baseada em Variáveis de Ambiente: Toda a autenticação e parametrização do sistema consome chaves nativas injetadas no ecossistema (.env), eliminando de forma definitiva a exposição de credenciais corporativas críticas em repositórios públicos de código.


---




import os
import sys
from dotenv import load_dotenv

# Garante que o Python encontre a pasta raiz 'src' ao rodar via terminal
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.database.neo4j_connection import Neo4jConnection

def run_ingestion():
    print("🚀 Iniciando o processo de ingestão de dados no Neo4j...")
    
    # 1. Inicializa a conexão com o banco
    try:
        db = Neo4jConnection()
    except Exception as e:
        print(f"❌ Erro ao conectar ao Neo4j Aura: {e}")
        print("Verifique se as variáveis de ambiente no arquivo .env estão corretas.")
        return

    # 2. Criação de Constraints (Garantia de Unicidade)
    print("🔒 Configurando restrições de unicidade (Constraints)...")
    constraints = [
        "CREATE CONSTRAINT cliente_cpf IF NOT EXISTS FOR (c:Cliente) REQUIRE c.cpf IS UNIQUE;",
        "CREATE CONSTRAINT dispositivo_id IF NOT EXISTS FOR (d:Dispositivo) REQUIRE d.device_id IS UNIQUE;",
        "CREATE CONSTRAINT conta_pix IF NOT EXISTS FOR (p:ContaDestino) REQUIRE p.pix IS UNIQUE;"
    ]
    
    for query in constraints:
        db.query(query)

    # 3. Limpeza do banco de dados (Garante idempotência ao rodar o script)
    print("🧹 Limpando registros antigos para evitar duplicidade...")
    db.query("MATCH (n) DETACH DELETE n;")

    # 4. Ingestão de Nós (Nodes)
    print("👥 Criando nós de Clientes, Dispositivos e Contas Destino...")
    nodes_query = """
    CREATE 
      (c1:Cliente {cpf: '11111111111', nome: 'João Silva'}),
      (c2:Cliente {cpf: '22222222222', nome: 'Maria Souza'}),
      (c3:Cliente {cpf: '33333333333', nome: 'Pedro Santos'}),
      (c4:Cliente {cpf: '44444444444', nome: 'Lucas Oliveira'}),
      
      (d1:Dispositivo {device_id: 'IPHONE999', ip: '192.168.1.10'}),
      (d2:Dispositivo {device_id: 'ANDROID123', ip: '192.168.1.11'}),
      
      (p1:ContaDestino {pix: 'fraude@pix.com', banco: 'Banco X'}),
      (p2:ContaDestino {pix: 'aluguel@pix.com', banco: 'Banco Y'})
    """
    db.query(nodes_query)

    # 5. Ingestão de Relacionamentos (Criação da Teia Suspeita)
    print("🔗 Amarrando relacionamentos e simulando transações bancárias...")
    relationships_query = """
    // Conectando os CPFs suspeitos ao mesmo dispositivo físico (Vetor de Fraude 1)
    MATCH (c1:Cliente {cpf: '11111111111'}), (d1:Dispositivo {device_id: 'IPHONE999'}) CREATE (c1)-[:UTILIZA]->(d1);
    MATCH (c2:Cliente {cpf: '22222222222'}), (d1:Dispositivo {device_id: 'IPHONE999'}) CREATE (c2)-[:UTILIZA]->(d1);
    MATCH (c3:Cliente {cpf: '33333333333'}), (d1:Dispositivo {device_id: 'IPHONE999'}) CREATE (c3)-[:UTILIZA]->(d1);
    
    // Conectando o usuário legítimo/comum ao seu próprio dispositivo
    MATCH (c4:Cliente {cpf: '44444444444'}), (d2:Dispositivo {device_id: 'ANDROID123'}) CREATE (c4)-[:UTILIZA]->(d2);

    // Simulando as transferências para a conta laranja do fraudador (Vetor de Fraude 2)
    MATCH (c1:Cliente {cpf: '11111111111'}), (p1:ContaDestino {pix: 'fraude@pix.com'}) 
    CREATE (c1)-[:TRANSFERIU {valor: 5000.00, data: '15/06/2026'}]->(p1);
    
    MATCH (c2:Cliente {cpf: '22222222222'}), (p1:ContaDestino {pix: 'fraude@pix.com'}) 
    CREATE (c2)-[:TRANSFERIU {valor: 4500.00, data: '15/06/2026'}]->(p1);
    
    MATCH (c3:Cliente {cpf: '33333333333'}), (p1:ContaDestino {pix: 'fraude@pix.com'}) 
    CREATE (c3)-[:TRANSFERIU {valor: 5500.00, data: '15/06/2026'}]->(p1);

    // Transação legítima isolada
    MATCH (c4:Cliente {cpf: '44444444444'}), (p2:ContaDestino {pix: 'aluguel@pix.com'}) 
    CREATE (c4)-[:TRANSFERIU {valor: 1200.00, data: '15/06/2026'}]->(p2);
    """
    db.query(relationships_query)

    print("✅ Ingestão finalizada com sucesso! O grafo está pronto para testes.")

if __name__ == "__main__":
    # Carrega o arquivo .env da raiz do projeto
    load_dotenv()
    run_ingestion()

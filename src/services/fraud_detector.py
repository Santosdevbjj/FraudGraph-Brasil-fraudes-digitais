from src.database.neo4j_connection import Neo4jConnection

class FraudDetector:
    def __init__(self):
        self.db = Neo4jConnection()

    def detect_high_risk_patterns(self):
        """
        Query Coração do Projeto: Identifica se múltiplos CPFs utilizam o mesmo
        dispositivo E enviaram dinheiro para a mesma conta Pix (Triangulação de Fraude).
        """
        query = """
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
        """
        return self.db.query(query)

from database.neo4j_connection import Neo4jConnection

class FraudDetector:

    def __init__(self):

        self.db = Neo4jConnection()

    def detect_shared_devices(self):

        query = """
        MATCH (c:Cliente)-[:UTILIZA]->(d:Dispositivo)

        WITH d,
        collect(c.nome) as clientes,
        count(c) as total

        WHERE total > 1

        RETURN d.device_id,
               clientes,
               total
        """

        return self.db.query(query)

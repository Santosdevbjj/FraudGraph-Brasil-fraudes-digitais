from neo4j import GraphDatabase
import os

class Neo4jConnection:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(
                os.getenv("NEO4J_USER"),
                os.getenv("NEO4J_PASSWORD")
            )
        )

    def query(self, query):

        with self.driver.session() as session:
            result = session.run(query)

            return [r.data() for r in result]

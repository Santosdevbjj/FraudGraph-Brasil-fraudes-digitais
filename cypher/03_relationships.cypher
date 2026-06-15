MATCH (c:Cliente {cpf:'11111111111'})
MATCH (d:Dispositivo {device_id:'IPHONE999'})
CREATE (c)-[:UTILIZA]->(d);

MATCH (c:Cliente {cpf:'22222222222'})
MATCH (d:Dispositivo {device_id:'IPHONE999'})
CREATE (c)-[:UTILIZA]->(d);

MATCH (c:Cliente {cpf:'33333333333'})
MATCH (d:Dispositivo {device_id:'IPHONE999'})
CREATE (c)-[:UTILIZA]->(d);

MATCH (c:Cliente)-[:UTILIZA]->(d:Dispositivo)

WITH d,
collect(c.nome) as clientes,
count(c) as total

WHERE total > 1

RETURN
d.device_id,
clientes,
total 






MATCH
(c:Cliente)-[:UTILIZA]->(d:Dispositivo),

(c)-[:TRANSFERIU]->(p:ContaDestino)

WITH
d,
p,
collect(c.nome) as clientes,
count(c) as total

WHERE total >= 3

RETURN
d.device_id,
p.pix,
clientes,
total 




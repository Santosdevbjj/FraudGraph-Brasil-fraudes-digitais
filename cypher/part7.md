

Criando Agentes no Neo4j Aura › Criando um Agente
Adicionar uma ferramenta Text2Cypher

Sérgio
Agentes de construção no Neo4j Aura

Introdução ao Aura Agent
Introdução ao Aura Agent
Agentes de design e gestão
Crie seu primeiro agente
(Opcional)
Construindo um Agente
Ferramentas para criação de modelos de cifra
Crie sua própria ferramenta de modelo Cypher
Utilizando Text2Cypher para consultas ad-hoc
Adicionar uma ferramenta Text2Cypher
Utilizando a ferramenta de Busca por Similaridade
Agentes editoriais
Publicar um agente
Conecte seu agente ao Cursor
(Opcional)
Próximos passos

Português (Brasil)
Powered by Google TradutorTradutor
Desafio
Adicionar uma ferramenta Text2Cypher
Neste desafio, você deverá identificar uma questão que suas ferramentas atuais não conseguem responder, criar uma ferramenta Text2Cypher para lidar com ela e verificar a cifra gerada no painel de raciocínio.

Passo 1: Encontre uma pergunta que suas ferramentas não consigam responder.
Pense em uma pergunta que seu agente não consegue responder de forma confiável com as ferramentas existentes — uma pergunta cuja estrutura depende do que está sendo perguntado, como agregações de múltiplos saltos, filtros dinâmicos ou combinações que seus modelos Cypher não abrangem.

Se você estiver usando o Northwind, experimente uma destas opções:

Which customers ordered products from more than two different suppliers?

Which products are in both the Beverages and Condiments categories?

List the top three customers by total order value.

Faça a pergunta no painel de pré-visualização e anote a resposta. O agente pode recusar, chutar ou retornar uma resposta incompleta. Você fará a mesma pergunta novamente na Etapa 3, após adicionar uma ferramenta específica, para comparar a diferença.

Etapa 2: Criar uma ferramenta Text2Cypher
Abra a configuração do agente e adicione uma nova ferramenta Text2Cypher .

Defina o nome como algo descritivo que reflita sua finalidade, por exemploAnswer Customer Questions...

Na descrição , indique ao agente quando usar a ferramenta e forneça o contexto do domínio para ajudá-lo a gerar um código Cypher preciso:

Quando usar : quando nenhuma outra ferramenta abrange a questão e é necessária uma consulta gerada dinamicamente.

Contexto do domínio : o agente já recebe o esquema completo do banco de dados automaticamente — não liste todos os rótulos e tipos de relacionamento. Em vez disso, adicione o contexto que o esquema não fornece: o formato dos identificadores (por exemplo, "IDs de clientes são códigos em maiúsculas como ALFKI"), quais valores de propriedades categóricas são úteis para filtragem e quais propriedades numéricas são adequadas para agregação.

Para a Northwind, o contexto de domínio relevante inclui o fato de que os IDs dos clientes são códigos em maiúsculas (ALFKI, QUICK), que `id` unitPricee quantity`value` são propriedades numéricas adequadas para agregação e que ` freightcost` é um campo de custo nos pedidos.

Salve a ferramenta e clique em Atualizar agente .

Passo 3: Faça a pergunta novamente e compare.
No painel de pré-visualização, faça a mesma pergunta da Etapa 1.

Expanda a seção "Pensamento" e encontre a entrada "Aplicando ferramenta de agente" para sua ferramenta Text2Cypher. Compare os resultados com as ferramentas existentes:

Código Cypher gerado : Ele usa os rótulos e tipos de relacionamento corretos para o seu grafo?

Resultado : O conjunto de resultados corresponde ao que você esperava?

Mais importante ainda, fornece uma resposta mais precisa do que as ferramentas existentes?

Se o Cypher gerado usar rótulos ou tipos de relacionamento incorretos, edite a descrição da ferramenta para adicionar ou esclarecer o contexto do domínio e, em seguida, faça a pergunta novamente.

Marcar como concluído
60%
Utilizando Text2Cypher para consultas ad-hoc
Utilizando a ferramenta de Busca por Similaridade
Esta página foi útil?SimNão



 

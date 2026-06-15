

Criando Agentes no Neo4j Aura › Criando um Agente
Crie sua própria ferramenta de modelo Cypher

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
Crie sua própria ferramenta de modelo Cypher
Agora você sabe quando e como usar as ferramentas de modelo Cypher.

Neste desafio, você adicionará uma ferramenta de modelo Cypher ao agente que criou no primeiro módulo.

Meta
Crie uma ferramenta de modelo Cypher que permita ao seu agente responder a uma pergunta que ele não consiga resolver adequadamente apenas com as ferramentas geradas. Escolha um tipo de pergunta que se encaixe no seu grafo, escreva o código Cypher, defina o parâmetro e teste-o.

Antes de começar
Conclua a lição anterior, Introdução ao Aura Agent, e o desafio Criar um Agente com IA para ter um agente em seu próprio grafo ou no Northwind.

Abra esse agente no Console do Aura: Serviços de Dados → Agentes e selecione o seu agente.

Clique em Adicionar Ferramenta → Modelo de Cifra para começar a adicionar uma nova ferramenta.

Adicionar menu de ferramentas com opção de modelo Cypher
Sua tarefa
Adicione uma ferramenta de modelo Cypher. Você decide:

Qual pergunta ele responde ?
Por exemplo: obter uma entidade por ID ou nome, listar itens em uma categoria ou os N principais por alguma métrica. Adapte-o ao seu esquema.

Os parâmetros necessários são :
nome, tipo e descrição.

Consulta Cypher :
Lembre-se de usar marcadores de posição de parâmetros, como $parameter_namepara os valores que o LLM irá extrair.

Diretrizes:

A descrição da ferramenta indica ao profissional de Direito quando utilizá-la. Seja específico quanto ao tipo de questão.

A descrição do parâmetro informa ao LLM qual valor extrair. Inclua um valor de exemplo: para Northwind, você pode usar "O ID do cliente, por exemplo, ALFKI ou QUICK," ou o equivalente para o seu gráfico.

Se você não tiver certeza sobre o esquema, teste seu Cypher na ferramenta de consulta primeiro. No Console do Aura, abra Ferramentas → Consulta para visualizar o painel de informações do banco de dados com rótulos de nós, tipos de relacionamento e chaves de propriedade e, em seguida, execute seu Cypher.

Ferramenta de exemplo: Obtenção de clientes e pedidos no Northwind
Teste sua ferramenta
Após salvar sua ferramenta, clique em Atualizar agente para aplicar as alterações.

Página de configuração do agente mostrando o botão Atualizar agente
Em seguida, faça uma pergunta que deve acionar sua nova ferramenta. Expanda a seção Pensamento para confirmar se o agente a selecionou e se passou o valor de parâmetro correto.

Marcar como concluído
47%
Ferramentas para criação de modelos de cifra
Utilizando Text2Cypher para consultas ad-hoc
Esta página foi útil?SimNão



 



Construindo Agentes no Neo4j Aura › Introdução ao Agente Aura
Agentes de design e gestão

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
Lição
Agentes de design e gestão
Para construir um agente eficaz, você precisa de um projeto claro.

Um agente com ferramentas mal definidas, descrições vagas ou falta de contexto de relacionamento apresentará resultados inconsistentes mesmo com dados de boa qualidade.

Nesta lição, você aprenderá como definir função e escopo, mapear tipos de perguntas para o Modelo Cypher ou Text2Cypher, escrever descrições de ferramentas para que o LLM selecione a ferramenta correta e editar, excluir e gerenciar ferramentas e agentes.

Função e âmbito de atuação
Defina o que o agente faz e, igualmente importante, o que ele não faz.

Um agente focado em uma tarefa específica funciona melhor do que um agente de propósito geral. Um escopo restrito facilita a seleção de ferramentas para o LLM e torna o comportamento do agente mais previsível.

Por exemplo, um agente Northwind Analyst responde a perguntas sobre clientes, pedidos, produtos, categorias e fornecedores. Ele não responde a perguntas sobre estratégia de preços, RH ou qualquer coisa fora do gráfico.

Codificar esse limite nas instruções mantém o agente focado na tarefa. Por exemplo, instrua-o a recusar educadamente solicitações fora do tópico.

Tipos de perguntas
Antes de criar ferramentas, decida qual tipo de ferramenta se adequa a cada pergunta que seu agente precisa responder.

A estrutura da consulta é fixa?
Se o MATCHpadrão, WHEREas condições e RETURNa cláusula forem todos conhecidos antecipadamente e apenas os valores mudarem, use um modelo Cypher .

Por exemplo, "Os 10 principais clientes por número de pedidos" tem um valor fixo para COUNT, ORDER BY, e LIMIT $n— escreva-o como um modelo. Os modelos Cypher funcionam bem para perguntas previsíveis e repetíveis e podem usar padrões de múltiplos saltos para recuperar dados em todo o grafo.

A estrutura da consulta muda a cada pergunta?
Se a consulta não puder ser pré-escrita porque a própria estrutura depende do que o usuário solicita, use Text2Cypher .

Por exemplo, "Quais clientes encomendaram produtos de mais de 2 fornecedores diferentes?" — a quantidade de filtros, o caminho com múltiplos saltos e a agregação variam de acordo com a pergunta.

A pergunta é vaga ou aberta?
Se a pergunta for exploratória e puder ser respondida encontrando nós semanticamente semelhantes à entrada do usuário, use uma ferramenta de Busca por Similaridade .

Por exemplo, "Quais produtos são semelhantes ao chá chai?" ou "Encontre fornecedores que trabalham com laticínios". Essas perguntas não têm uma estrutura Cypher fixa e não procuram um valor específico conhecido — elas precisam de busca vetorial para encontrar correspondências relevantes.

A Busca por Similaridade exige que os nós do seu grafo tenham representações vetoriais armazenadas como propriedades e um índice vetorial construído com base nessas representações. Gerar representações vetoriais significa converter propriedades de texto em vetores numéricos usando um modelo de incorporação — esta é uma etapa separada de preparação de dados antes de configurar a ferramenta.

Para saber mais, consulte Introdução aos índices vetoriais e dados não estruturados .

Descrição das ferramentas
O LLM seleciona ferramentas com base exclusivamente em suas descrições. Ele nunca inspeciona a consulta Cypher ou os nomes dos parâmetros. Uma descrição como "obter dados do cliente" é vaga demais para ser útil: se três ferramentas recuperam dados, o LLM não tem base para escolher entre elas.

Escreva descrições que respondam a duas perguntas:

O que essa ferramenta retorna?

Quando o mestrado em Direito (LLM) deve usar essa ferramenta em vez das outras?

Compare estas duas descrições para a mesma ferramenta:

Descrição	Problema
Get customer data

Muito vago: poderia corresponder a qualquer pergunta que mencionasse um cliente.

Return customer details and recent orders for a specific customer ID, for example ALFKI

Especifica: nomeia o tipo do parâmetro, fornece um valor de exemplo e define o escopo do que ele retorna.

Para o seu recurso de fallback Text2Cypher, a descrição deve indicar quando usá-lo (e quando não usá-lo). A ferramenta recebe automaticamente o esquema do banco de dados. Adicione contexto específico do domínio: entidades relevantes, padrões de propriedades categóricas e quais atributos são adequados para agregação. Isso ajuda o LLM a gerar um Cypher mais preciso.

texto

Cópia
Use this tool ONLY when no other tool covers the question.
The graph contains: Customer, Order, Product, Category, Supplier nodes.
Relationships: PLACED (Customer→Order), CONTAINS (Order→Product), IN_CATEGORY (Product→Category), SUPPLIES (Supplier→Product).
A restrição "SOMENTE quando nenhuma outra ferramenta for adequada" impede que o LLM use o Text2Cypher por padrão para perguntas que seus modelos abordam.

Criar um agente
Depois de definir a função, o escopo e o conjunto de ferramentas para o seu agente, você o cria no Console do Aura em Serviços de Dados → Agentes → Criar Agente → Criar do zero .

O menu Criar Agente exibe as opções Criar do zero e Criar com IA.
Dê um nome ao agente, conecte-o à sua instância do AuraDB e escreva instruções que definam sua função, escopo e o que deve ser recusado.

Criar do zero uma caixa de diálogo que mostre o nome
Adicionando uma ferramenta
Com o agente aberto, clique em Adicionar Ferramenta e selecione o tipo de ferramenta: Modelo de Criptografia , Texto para Criptografia ou Busca por Similaridade .

Menu Adicionar Ferramenta mostrando o Modelo de Cifra
Preencha o nome, a descrição e qualquer configuração necessária para esse tipo de ferramenta. Depois de adicionar ou alterar ferramentas, clique em Atualizar agente para salvar — o agente continuará usando a configuração anterior até que você faça isso.

Editando uma ferramenta
Clique no ícone de lápis ao lado de qualquer ferramenta para abrir a caixa de diálogo de edição. Você pode atualizar o nome, a descrição, os parâmetros e a consulta Cypher.

Lista de ferramentas mostrando o ícone de lápis para editar e o ícone de lixeira para excluir uma ferramenta.
Para as ferramentas de modelo Cypher, clique no ícone de lápis ao lado de um parâmetro para atualizar seu nome, tipo de dados ou descrição.

Diálogo de edição de parâmetros exibindo o nome.
Clique em Atualizar agente após qualquer alteração para salvar.

Excluindo uma ferramenta
Clique no ícone da lixeira ao lado de uma ferramenta para removê-la e, em seguida, clique em Atualizar agente para confirmar a alteração.

Excluindo um agente
Abra o menu …​ ao lado do agente na lista de Agentes e selecione Excluir agente .

Lista de agentes exibindo o menu de contexto com a opção Novo Chat
Diálogo de confirmação de exclusão do agente informando que a ação é permanente e não pode ser desfeita.
A exclusão é permanente.

A exclusão de um agente é irreversível. Todas as ferramentas, instruções e configurações são removidas permanentemente.

Criando um agente com IA
O Aura Agent também oferece uma opção de Criação com IA . Em vez de configurar um agente manualmente, você fornece um prompt descrevendo a função e o escopo do agente, e a plataforma lê o esquema da sua instância e gera um conjunto de ferramentas automaticamente.

Isso é útil para começar rapidamente — a IA produz um conjunto inicial de ferramentas que você pode revisar, editar e aprimorar usando as mesmas técnicas abordadas nesta lição.

No próximo desafio, você usará o Create with AI para construir seu primeiro agente e, em seguida, avaliará as ferramentas geradas por ele em relação aos princípios de design aqui apresentados.

Verifique se você entendeu.
Escopo restrito
Por que é importante definir um papel e um escopo claros ao projetar um agente?

Selecione a resposta correta.

 Isso permite que o agente responda ao máximo de perguntas possível.
 Isso ajuda o LLM a escolher ferramentas com mais facilidade e torna o comportamento do agente mais previsível.
 Isso garante que o agente sempre use Text2Cypher quando o modo de pensamento estiver ativado.
 Isso impede que o agente use consultas Cypher.
Confira a resposta
20%
Introdução ao Aura Agent
Crie seu primeiro agente
Esta lição foi útil?SimNão



 

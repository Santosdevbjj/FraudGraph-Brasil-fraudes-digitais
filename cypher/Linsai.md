

Construindo Agentes no Neo4j Aura › Introdução ao Agente Aura
Introdução ao Aura Agent

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
Introdução ao Aura Agent
O Aura Agent permite criar sistemas de recuperação que consultam seu grafo de conhecimento a partir do Console Aura sem escrever código.

Nesta lição, você aprenderá:

O que é um Agente Aura?

Quando usar o Aura Agent

Como funciona o Aura Agent

O que é o Agente Aura?
O Aura Agent é uma plataforma de pouco ou nenhum código no Aura Console que permite criar agentes de IA capazes de transformar perguntas em linguagem natural em consultas gráficas que são executadas em seus dados no AuraDB.

Você conecta um agente a uma instância do AuraDB que contém seus dados de grafo. Quando um usuário faz uma pergunta, o agente interpreta a solicitação, recupera os dados relevantes do grafo e retorna o resultado. Você pode criar, testar e refinar agentes visualmente no Console — sem precisar escrever código de aplicativo.

O Aura Agent é útil quando você deseja criar agentes que recuperam dados do seu grafo de conhecimento AuraDB usando linguagem natural, permitindo que os desenvolvedores criem assistentes de IA baseados em seus dados do grafo.

Como funciona o Aura Agent
Cada agente segue um ciclo de processamento para analisar uma solicitação, decidir o que fazer em seguida, executar as ferramentas adequadas e retornar uma resposta fundamentada.

Em vez de partir diretamente para uma resposta, o agente orquestra uma sequência de etapas:

Interpretar a entrada do usuário : Compreender a pergunta do usuário, identificar o objetivo e determinar quais informações são necessárias.

Planeje os próximos passos : Decida qual ferramenta ou ferramentas usar e em que ordem.

Executar ferramentas : Execute a(s) ferramenta(s) selecionada(s) para ler dados do seu grafo. O agente pode chamar várias ferramentas, usando a saída de uma etapa para orientar a próxima.

Gerar resposta : Utilize os dados obtidos para produzir uma resposta em linguagem natural fundamentada no grafo.

Esse processo iterativo — interpretar, planejar, executar e avaliar — se repete até que o agente tenha informações suficientes para responder.

Ferramentas disponíveis
Seu Agente Aura pode ser equipado com três tipos de ferramentas de recuperação de dados somente leitura para consultar seu grafo. Cada tipo de ferramenta foi projetado para um padrão de consulta diferente, permitindo que você defina a maneira apropriada de lidar com tipos específicos de solicitações de usuários.

Modelo de cifra
Uma ferramenta de modelo Cypher executa uma consulta Cypher predefinida e parametrizada em seu banco de dados. O agente extrai os valores dos parâmetros da pergunta do usuário e os passa para a consulta em tempo de execução.

Utilize esta ferramenta quando uma pergunta puder ser respondida com uma consulta conhecida e repetível — por exemplo, "Obter ALFKI do cliente". Essa abordagem proporciona desempenho e controle previsíveis, pois a estrutura da consulta é fixa antecipadamente.

Busca por similaridade
Uma ferramenta de Busca por Similaridade encontra nós com base na similaridade semântica usando busca vetorial.

Use esta ferramenta quando quiser encontrar entidades relacionadas ou semelhantes — por exemplo, "Quais produtos são semelhantes ao chá?". Esta ferramenta requer:

Um índice vetorial criado em sua instância do AuraDB.

Dados gráficos preenchidos com representações vetoriais geradas a partir de um modelo de incorporação de texto compatível.

O agente utiliza o índice para comparar representações vetoriais e retornar os nós semanticamente mais semelhantes.

Texto para Criptografia
A ferramenta Text2Cypher gera código Cypher a partir de linguagem natural em tempo de execução e o executa em seu grafo.

Use esta ferramenta quando a pergunta não for contemplada por um Modelo Cypher existente ou por uma ferramenta de Busca por Similaridade — por exemplo, "Quais são os 10 principais produtos por receita em todas as categorias?". Esta ferramenta oferece flexibilidade, permitindo que o agente crie consultas dinamicamente com base na solicitação do usuário.

Pré-requisitos para executar Aura Agents
Para usar o Aura Agent, certifique-se de que ambas as opções a seguir estejam habilitadas nas configurações da sua organização :

Assistência de IA generativa

Agente Aura . Você pode ativar e desativar essa opção quando a assistência de IA generativa estiver habilitada.

Se o agente não conseguir se conectar à instância, verifique se a autenticação de ferramentas está habilitada para o projeto. Essa configuração é feita em Segurança, no nível da organização. A autenticação de ferramentas está habilitada por padrão para organizações criadas após maio de 2025. Para organizações mais antigas, habilite-a, se necessário. Consulte a documentação do Aura Agent para obter informações sobre os pré-requisitos.

Antes de iniciar o curso, verifique se ambas as opções estão ATIVADAS . Este curso utiliza a criação manual de agentes no Console Aura: Criar com IA e Criar do zero. Os agentes estão em Serviços de Dados → Agentes no Console Aura.

Configurações mostrando a opção Agente Aura ativada
Para criar um agente, você precisa ser um Administrador de Projeto .

Verificando sua função no projeto
O acesso dos agentes é controlado por funções do projeto. Não existem funções dedicadas ao nível do agente.

Papel	Permissões
Espectador e membro

É possível listar e invocar todos os agentes do projeto.

Administrador do Projeto

Também é possível criar, atualizar e excluir agentes.

Para verificar sua função, acesse Projeto → Usuários na navegação à esquerda do Console do Aura:

Navegação à esquerda do Aura Console com Projetos expandidos e Usuários destacados.
Sua função está listada na coluna "Função no projeto" ao lado do seu endereço de e-mail:

Lista de usuários do projeto mostrando o usuário
Para dar acesso a um agente a um membro da equipe, adicione-o ao projeto Aura com a função apropriada.

Verifique se você entendeu.
Escopo do Agente Aura
Qual das seguintes opções não é algo que um Agente Aura faz ao lidar com uma pergunta do usuário?

Selecione a resposta correta.

 Descubra o que o usuário precisa e qual ou quais ferramentas usar.
 Execute as ferramentas selecionadas no gráfico (pode ser que mais de uma seja executada).
 Insira dados novos ou atualizados no gráfico usando ferramentas.
 Utilize os dados recuperados para produzir uma resposta em linguagem natural.
Tipos de ferramentas do Aura Agent
Quais dos seguintes são tipos de ferramentas que um Agente Aura pode usar para consultar seu grafo? (Selecione todas as opções aplicáveis)

 Modelo de cifra
 Texto para Criptografia
 Busca por similaridade
 A ferramenta de importação
Confira as respostas
13%
Introdução ao Aura Agent
Agentes de design e gestão
Esta lição foi útil?SimNão




Texto original
Your Aura Agent can be equipped with three types of read-only data retrieval tools to query your graph. Each tool type is designed for a different query pattern, allowing you to define the appropriate way to handle specific types of user requests.
Avalie a tradução
O feedback vai ser usado para ajudar a melhorar o Google Tradutor























---



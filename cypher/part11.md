

Construindo Agentes no Neo4j Aura › Publicando Agentes
Próximos passos

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
Próximos passos
Parabéns por concluir o curso Aura Agent!

Você aprendeu como projetar, construir e publicar agentes de IA que respondem a perguntas em linguagem natural usando seu grafo de conhecimento Neo4j — sem escrever código de aplicativo.

Entendendo o Agente Aura
Agora você sabe como:

Explique o que é o Aura Agent e como ele se integra ao Aura Console.

Descreva o ciclo do agente: interpretar a entrada, selecionar uma ferramenta, executar uma consulta, gerar uma resposta.

Identifique qual dos três tipos de ferramentas — Modelo de Criptografia, Texto para Criptografia ou Busca por Similaridade — se adequa a cada tipo de pergunta.

Defina a função e o escopo para que o agente se mantenha focado e recuse solicitações fora do tópico.

Escreva descrições de ferramentas que forneçam ao profissional de saúde mental contexto suficiente para selecionar a ferramenta correta.

Ferramentas de construção
Agora você sabe como:

Crie uma ferramenta de modelo Cypher com consultas parametrizadas e nomes de parâmetros descritivos.

Crie uma ferramenta Text2Cypher com uma descrição que respeite o domínio de aplicação e limite seu uso.

Entenda quando a Busca por Similaridade se aplica e qual preparação de grafo ela exige.

Adicione, edite e exclua ferramentas e salve as alterações com o agente de atualização.

Use o painel de raciocínio para verificar a seleção da ferramenta e inspecionar o código cifrado gerado.

Publicar e conectar
Agora você sabe como:

Escolha entre os modos de acesso interno e externo.

Habilite o servidor MCP e recupere o endpoint MCP.

Conecte seu agente a um cliente MCP, como o Cursor ou o Claude Desktop.

Melhores práticas
Defina o escopo dos agentes de forma restrita — Um agente focado por tarefa facilita a seleção de ferramentas para o LLM e torna o comportamento mais previsível. Inclua uma instrução para recusar solicitações fora do tópico.

Primeiro, use modelos — Se você conseguir escrever a consulta Cypher completa agora, usando apenas $parameteros espaços para os valores das variáveis, utilize um modelo Cypher. Reserve o Text2Cypher para perguntas cuja estrutura se altera.

Escreva descrições eficazes para o Text2Cypher — indique quando usar a ferramenta e quando não (por exemplo, somente quando nenhum modelo for adequado). Adicione contexto de domínio: rótulos de nós relevantes, relacionamentos e quais propriedades são adequadas para filtragem e agregação.

Uma ferramenta por padrão de pergunta — Atribua a cada tipo de pergunta distinto sua própria ferramenta. Um modelo único que tenta abranger perguntas não relacionadas leva a descrições vagas e escolhas de ferramentas inadequadas.

Descreva os parâmetros como instruções — Escreva descrições de parâmetros com exemplos, como "O ID do cliente, por exemplo, ALFKI ou QUICK", e não apenas "O ID do cliente".

Use o painel de raciocínio — Sempre verifique o rastreamento de raciocínio para confirmar qual ferramenta foi selecionada e qual Cypher foi gerado. Inspecione a saída do Text2Cypher antes de utilizá-la em produção.




   
Salvar alterações — Depois de adicionar, editar ou excluir ferramentas, clique em Atualizar agente para persistir a configuração.

Pronto para o seu próximo desafio?
Para aprofundar seus conhecimentos em IA baseada em grafos e MCP:

Fundamentos do Neo4j e GenAI — Compreenda os fundamentos da IA ​​generativa e como o Neo4j se integra aos LLMs.

Utilizando o Neo4j com o LangChain — Integre o Neo4j com o LangChain para geração e agentes aprimorados por recuperação de informações.

Desenvolvimento com as ferramentas Neo4j MCP — Aprenda a usar o Protocolo de Contexto de Modelo (MCP) para conectar aplicações de IA às ferramentas e fontes de dados do Neo4j.

Criando ferramentas GraphRAG Python MCP — Crie seu próprio servidor GraphRAG MCP com ferramentas baseadas em grafos usando o SDK Python do MCP.

Criando ferramentas GraphRAG TypeScript para MCP — Crie suas próprias ferramentas e servidor MCP usando o SDK TypeScript para MCP.

Introdução a índices vetoriais e dados não estruturados — Aprenda como gerar embeddings e construir índices vetoriais para busca por similaridade.

Marcar como concluído
93%
Conecte seu agente ao Cursor
Esta lição foi útil?SimNão



Texto original
Ready for your next challenge?
Avalie a tradução
O feedback vai ser usado para ajudar a melhorar o Google Tradutor


---





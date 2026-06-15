

Construindo Agentes no Neo4j Aura ›
Agentes editoriais

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
Agentes editoriais
Neste módulo, você publicará seu agente para que ele possa ser chamado por agentes e aplicativos externos.

Ao final deste módulo, você será capaz de:

Compare o acesso interno e externo e escolha o modo mais adequado para o seu caso de uso.

Ative o servidor MCP

Conecte seu agente ao Cursor usando o endpoint MCP e teste-o com prompts reais.

Preparados? Vamos lá →

73%
Utilizando a ferramenta de Busca por Similaridade
Publicar um agente




---





Construindo Agentes no Neo4j Aura › Publicando Agentes
Publicar um agente

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
Publicar um agente
Até agora neste curso, você criou e testou um agente no Console Aura.

Nesta lição, você aprenderá como publicar seu agente e disponibilizá-lo para aplicativos externos por meio da API REST e do MCP.

Acesso interno e externo
Ao criar um agente, ele inicia no modo interno . Somente membros do seu projeto Aura podem usá-lo, e apenas através do painel de pré-visualização do Aura Console. Não há endpoint público nem custos adicionais.

Configurações de acesso mostrando a opção Interna selecionada
A mudança para o modo Externo expõe a API HTTP do agente, permitindo que aplicativos externos ao seu projeto Aura a acessem.

Agentes externos estão sujeitos a cobranças baseadas no uso. Consulte a documentação do Aura Agent para obter informações sobre preços.

Existem duas maneiras de integrar um agente externo: a API REST e o servidor MCP .

API REST
Quando o acesso externo está ativado, seu agente expõe um endpoint HTTP. Os aplicativos o acessam com uma solicitação POST e recebem uma resposta JSON — nenhum cliente MCP é necessário.

Para acessar o endpoint, você precisa de três coisas:

Uma chave de API do Aura — gere uma em Configurações da conta → Chaves de API no Console do Aura. Salve o ID do cliente e o segredo do cliente; o segredo é exibido apenas uma vez.

Um token de portador — troque suas credenciais por um token de acesso (válido por uma hora):

bash

Cópia
export BEARER_TOKEN=$(curl -s --request POST 'https://api.neo4j.io/oauth/token' \
    --user "$CLIENT_ID:$CLIENT_SECRET" \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'grant_type=client_credentials' | jq -r .access_token)
O URL do endpoint do agente — copie-o do menu …​ ao lado do seu agente na lista de Agentes. O URL tem este formato:


Cópia
https://api.neo4j.io/v2beta1/organizations/<org-id>/projects/<project-id>/agents/<agent-id>/invoke
Com essas informações em mãos, envie uma pergunta ao seu agente:

bash

Cópia
curl --request POST "$ENDPOINT_URL" \
 -H 'Content-Type: application/json' \
 -H 'Accept: application/json' \
 -H "Authorization: Bearer $BEARER_TOKEN" \
 -d '{"input": "Which are the top 5 most ordered products?"}' \
 --max-time 60
O agente retorna uma resposta JSON estruturada com a solução.

Habilitando o MCP
A mudança para o modo Externo também revela a opção Ativar servidor MCP .

As configurações de acesso mostram a opção "Externo" selecionada com a opção "Ativar servidor MCP" visível.
O Model Context Protocol (MCP) é um protocolo aberto para conectar aplicações de IA a ferramentas e fontes de dados externas. No MCP, um cliente é uma aplicação de IA como o Cursor ou o Claude Desktop, e um servidor expõe ferramentas que o cliente MCP pode descobrir e utilizar.

Habilitar essa opção inicia um servidor MCP que encapsula seu agente como uma ferramenta invocável, permitindo que os clientes MCP se conectem e o invoquem sem a necessidade de código de integração personalizado.

Tanto o acesso externo quanto a opção MCP devem estar ativados para clientes MCP; a API HTTP funciona apenas com a opção de acesso externo ativada.

Copiando o endpoint MCP
Após salvar com o servidor MCP ativado, abra o menu …​ ao lado do seu agente na lista de Agentes e selecione Copiar endpoint do servidor MCP .

Menu de contexto do agente exibindo as opções Copiar ponto de extremidade externo e Copiar ponto de extremidade do servidor MCP
O URL do endpoint é o que você cola na configuração do seu cliente MCP. Ele tem este formato:

texto

Cópia
https://mcp.neo4j.io/agent?project_id=<project-id>&agent_id=<agent-id>
Conectando o código de Claude
Adicione o endpoint ao Claude Code usando a CLI:

bash

Cópia
claude mcp add --transport http aura-agent https://mcp.neo4j.io/agent?project_id=<project-id>&agent_id=<agent-id>
Ou adicione-o manualmente ao seu ~/.claude.json:

json

Cópia
{
  "mcpServers": {
    "aura-agent": {
      "transport": "http",
      "url": "https://mcp.neo4j.io/agent?project_id=<project-id>&agent_id=<agent-id>"
    }
  }
}
Substitua os valores project_id`<endpoint>` agent_ide `<endpoint>` pelos valores do endpoint que você copiou. Na primeira vez que o Claude Code invocar o servidor, ele solicitará que você se autentique com suas credenciais do Aura.

Verifique se você entendeu.
Acesso interno vs. acesso externo
Você deseja consultar seu grafo a partir do Cursor ou de outro cliente MCP usando seu Agente Aura. Do que você precisa?

Selecione a resposta correta.

 Mantenha o agente com acesso interno. O cursor pode usar a pré-visualização do console.
 Configure o agente para acesso externo e habilite o servidor MCP.
 Crie uma chave de API separada. O modo de acesso não importa.
 Conceda ao seu colega de equipe a função de Membro do Projeto para que ele possa usar o agente.
Confira a resposta
80%
Agentes editoriais
Conecte seu agente ao Cursor
Esta lição foi útil?SimNão




Texto original
Replace the and values with those from the endpoint you copied. The first time Claude Code invokes the server it will prompt you to authenticate with your Aura credentials.
Avalie a tradução
O feedback vai ser usado para ajudar a melhorar o Google Tradutor  








   



Construindo Agentes no Neo4j Aura › Publicando Agentes
Conecte seu agente ao Cursor

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
Conecte seu agente ao Cursor
Neste desafio, você habilitará o acesso externo para seu agente, o conectará ao Cursor usando o endpoint MCP e o testará com prompts reais.

Habilitar acesso externo
Alterar as configurações de acesso requer a função de Administrador do Projeto .

Selecione seu agente e clique no menu … ​, depois selecione Configurar .

Menu do agente mostrando Configurar
Em Acesso , selecione Externo .

Ative a opção do servidor MCP .

As configurações de acesso mostram a opção "Externo" selecionada com a opção "Ativar servidor MCP" visível.
Clique em Atualizar agente para salvar suas alterações.

Seu agente agora possui um endpoint MCP e a lista completa de ferramentas está visível na configuração.

Configuração completa do agente, mostrando a opção "Ativar servidor MCP" habilitada, juntamente com a lista completa de ferramentas do agente.
Conectar ao cursor
Na lista de Agentes, abra o menu …​ ao lado do seu agente e escolha Copiar ponto de extremidade do servidor MCP .

Menu do agente mostrando Configurar
Abra o menu Cursor no canto superior esquerdo, depois Configurações… ​, e em seguida Configurações do Cursor .

Menu do cursor com Configurações e Configurações do cursor destacadas
Na barra lateral esquerda, selecione Ferramentas e MCP .

Em Servidores MCP instalados , clique em + Novo servidor MCP .

Ferramentas e configurações do MCP, mostrando os servidores MCP instalados e a opção Novo servidor MCP.
Um novo arquivo mcp.jsonserá criado (normalmente em ~/.cursor/mcp.json) e aberto no editor. Adicione o endpoint MCP do seu agente ao arquivo. Se você editar mcp.jsondiretamente, substitua <your-mcp-url>pelo endpoint do menu do agente:

json

Cópia
{
  "mcpServers": {
    "neo4j-graphacademy-agent": {
      "url": "<your-mcp-url>",
      "transport": "http"
    }
  }
}
Salve e recarregue o cursor.

Seu agente aparece na lista Ferramentas e MCP com o status Necessita de autenticação . Clique em Conectar .

Painel de ferramentas e MCP mostrando o agente neo4j-graphacademy com o status "Requer autenticação" e um botão "Conectar".
O cursor solicita permissão para abrir o site de autenticação do Aura MCP. Clique em Abrir .

Diálogo do macOS perguntando se deseja abrir o URL de autorização aura-mcp.eu.auth0.com em um navegador.
A página de login será aberta no seu navegador. Clique em Continuar com Neo4j Aura .

Página de login do aura-mcp exibindo um botão "Continuar com Neo4j Aura"
Na tela de autorização, clique em Aceitar para conceder ao Cursor acesso à sua conta Aura MCP.

A tela de autorização do aplicativo mostra o cursor solicitando acesso à conta aura-mcp com os botões Aceitar e Recusar.
Retorne ao cursor. Seu agente agora está conectado e disponível como ferramenta.

Para conectar outros clientes MCP, como o Claude Desktop, consulte a documentação do Aura Agent .

Teste seu agente no Cursor
Abra um novo chat do Cursor no modo Agente .

Dirija-se ao agente pelo nome do servidor MCP e faça uma pergunta que corresponda a uma das suas ferramentas de modelo Cypher.

Faça uma pergunta complementar que exija sua ferramenta Text2Cypher.

Verifique se cada resposta está correta e se o painel de raciocínio mostra a ferramenta correta selecionada.

Reinicie o Cursor antes de testar.

Reiniciar o Cursor após adicionar o endpoint MCP é obrigatório. Se o seu agente não estiver funcionando, a causa provável é a falta de reinicialização.

Marcar como concluído
87%
Publicar um agente
Próximos passos
Esta página foi útil?SimNão




Texto original
Address the agent by its MCP server name and ask a question that matches one of your Cypher Template tools.
Avalie a tradução
O feedback vai ser usado para ajudar a melhorar o Google Tradutor  


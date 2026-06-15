

Criando Agentes no Neo4j Aura › Criando um Agente
Utilizando Text2Cypher para consultas ad-hoc

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
Utilizando Text2Cypher para consultas ad-hoc
No desafio anterior, você criou uma ferramenta de Modelo Cypher que executa uma consulta Cypher fixa com parâmetros variáveis. Os Modelos Cypher funcionam bem quando a estrutura da consulta é conhecida antecipadamente, mas nem todas as perguntas se encaixam em um padrão predefinido.

Nesta lição você aprenderá como:

Decida quando usar o Text2Cypher em vez de um modelo Cypher.

Configure a ferramenta Text2Cypher para gerar consultas mais precisas.

Decidindo quando usar o Text2Cypher
A ferramenta Text2Cypher converte uma pergunta em linguagem natural em uma consulta Cypher em tempo de execução e a executa em seu grafo.

Com uma ferramenta Text2Cypher, seu agente pode se adaptar a perguntas que não seguem um padrão fixo.

O Text2Cypher usa um LLM (Low-Level Model) ajustado para gerar Cypher em tempo de execução, portanto a saída é probabilística. A mesma pergunta pode produzir Cypher diferentes em chamadas diferentes, e as consultas geradas podem conter erros.

Text2Cypher em produção

O Text2Cypher depende de um modelo de linguagem e pode gerar consultas com erros.

Teste as consultas geradas no painel de raciocínio antes de utilizá-las em produção.

Configurando uma ferramenta Text2Cypher
A ferramenta Text2Cypher possui duas opções de configuração: Nome e Descrição .

Diálogo de edição da ferramenta Text2Cypher exibindo os campos de nome e descrição.
Use o nome para identificar exclusivamente a ferramenta na configuração do agente.

Use a descrição para indicar ao agente quando usar e quando não usar a ferramenta. Inclua aspectos específicos do domínio do seu grafo, rótulos relevantes e tipos de relacionamento, além de quais atributos são adequados para agregação.

Invocando uma ferramenta Text2Cypher
Quando uma ferramenta Text2Cypher é invocada, o agente passa a pergunta do usuário, o esquema do banco de dados e o prompt do sistema Text2Cypher para o LLM. A instrução Cypher resultante é executada no grafo e os resultados são retornados ao usuário.

Você pode visualizar a declaração Cypher gerada e os resultados no painel de raciocínio.

Detalhe da ferramenta Text2Cypher mostrando a entrada em linguagem natural.
Verifique se você entendeu.
Nome da ferramenta
Qual a função da ferramenta Text2Cypher?

Selecione a resposta correta.

 É utilizado como o prompt do sistema enviado ao LLM.
 Ele controla qual esquema de banco de dados é fornecido à ferramenta.
 Ele identifica exclusivamente a ferramenta na configuração do agente.
 Isso determina quais perguntas a ferramenta responderá.
Descrição da ferramenta
O que você pode incluir na descrição da ferramenta Text2Cypher? Selecione todas as opções aplicáveis.

 O nome da sua instância
 Quando usar e quando não usar a ferramenta
 Aspectos específicos do domínio do seu gráfico
 Quais atributos são adequados para agregação ou filtragem?
 O esquema gráfico completo
Confira as respostas
53%
Crie sua própria ferramenta de modelo Cypher
Adicionar uma ferramenta Text2Cypher
Esta lição foi útil?SimNão



Texto original
Text2Cypher uses a fine-tuned LLM to generate Cypher at runtime, so the output is probabilistic. The same question can produce different Cypher on different calls, and generated queries may contain errors.
Avalie a tradução
O feedback vai ser usado para ajudar a melhorar o Google Tradutor


 



Construindo Agentes no Neo4j Aura ›
Construindo um Agente

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
Construindo um Agente
Neste módulo, você explorará as ferramentas geradas pela IA e ampliará seu agente com as ferramentas Cypher Template, Text2Cypher e Similarity Search.

Você irá:

Explique as ferramentas criadas pela IA e quando usar cada uma delas.

Adicione ferramentas de modelo Cypher para consultas previsíveis e repetíveis.

Adicionar uma ferramenta Text2Cypher para perguntas específicas

Entenda quando usar a Busca por Similaridade para pesquisas baseadas em vetores.

Preparados? Vamos lá →

33%
Crie seu primeiro agente  



--- 




Criando Agentes no Neo4j Aura › Criando um Agente
Ferramentas para criação de modelos de cifra

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
Ferramentas para criação de modelos de cifra
As ferramentas de modelo Cypher permitem que o agente execute consultas predefinidas com valores extraídos da pergunta do usuário.

Nesta lição você aprenderá como:

Defina um modelo Cypher com parâmetros nomeados.

Adicione uma ferramenta de modelo Cypher ao seu agente no console do Aura.

O que é um modelo de cifra?
Um modelo Cypher é uma consulta Cypher pré-escrita e parametrizada. Você define a consulta uma única vez e o LLM extrai os valores dos parâmetros da pergunta do usuário e a executa. As consultas usam $parametermarcadores nomeados. O LLM os preenche com os valores da pergunta do usuário em tempo de execução.

Use um modelo Cypher para perguntas comuns e repetidas com estrutura conhecida: "Obter ALFKI do cliente", "Listar produtos em Bebidas", "10 principais clientes por número de pedidos". Como a consulta é pré-escrita, os resultados são determinísticos: a mesma pergunta sempre executa o mesmo Cypher.

O que são parâmetros?
Os parâmetros são marcadores nomeados em uma consulta Cypher, prefixados com $. O LLM extrai o valor correto da entrada do usuário e o passa em tempo de execução.

Por exemplo, a seguinte consulta possui um parâmetro $customer_id:

cifra

Cópia
MATCH (c:Customer {id: $customer_id})
RETURN c.companyName, c.contactName, c.city
Quando um usuário pergunta "Obtenha o cliente ALFKI", o LLM extrai informações "ALFKI"da pergunta e executa a consulta com $customer_id = "ALFKI". O mesmo modelo lida com "Obtenha o cliente QUICK" substituindo "QUICK", sem a necessidade de uma nova consulta.

Um parâmetro pode ser de um dos quatro tipos: string, inteiro, ponto flutuante ou booleano.

Tipo	Parâmetro de exemplo	Exemplo de pergunta
corda

$customer_id

"Obter cliente ALFKI" →customer_id = "ALFKI"

inteiro

$limit

"Mostre-me os 5 principais clientes" →limit = 5

flutuador

$min_price

"Produtos acima de US$ 9,99" →min_price = 9.99

booleano

$discontinued

"Mostrar produtos descontinuados" →discontinued = true

Cada parâmetro precisa de um nome, um tipo de dados e uma descrição. O LLM usa a descrição para entender qual valor extrair.

Escreva descrições como instruções.

Uma descrição vaga como essa "The customer ID"dá ao mestrado em direito (LLM) pouca informação para trabalhar. Uma descrição específica como essa "The customer ID, for example ALFKI or QUICK"indica exatamente o que procurar e em qual formato.

Adicionando uma ferramenta de modelo Cypher
No Console do Aura, você adiciona um Modelo Cypher a partir da configuração do agente clicando em Adicionar Ferramenta → Modelo Cypher .

Menu Adicionar Ferramenta mostrando o Modelo de Cifra
A configuração da ferramenta exibe o nome, a descrição, os parâmetros e a consulta Cypher. Use o ícone de lápis para editar qualquer um desses campos.

Diálogo de edição da ferramenta Modelo de Cifra mostrando o nome
Para adicionar ou editar um parâmetro, abra a caixa de diálogo de parâmetros e defina o nome, o tipo de dados e a descrição.

Diálogo de edição de parâmetros exibindo o nome.
Lista de parâmetros mostrando os parâmetros salvos com ícones de edição e exclusão.
Melhores práticas para modelos de cifras
Use modelos Cypher para perguntas que você pode prever com antecedência — consultas comuns e repetidas com uma estrutura fixa. Cada modelo adicionado reduz a frequência com que o agente precisa gerar Cypher dinamicamente.

Para obter o melhor desempenho, as consultas de modelo Cypher devem:

Retorna apenas as propriedades escalares relevantes — não nós inteiros, relacionamentos, caminhos ou incorporações.

Evite linhas duplicadas

Limitar os resultados a 10–50 linhas para manter as respostas focadas

Por exemplo, use RETURN c.id, c.companyNameem vez de RETURN c.

Verifique se você entendeu.
Papel de um parâmetro
Qual é a função de um parâmetro em uma ferramenta de modelo Cypher?

Selecione a resposta correta.

 Ele extrai as frases do usuário e as incorpora diretamente na string Cypher.
 É um marcador nomeado cujo valor o LLM extrai da pergunta do usuário em tempo de execução.
 Define qual ferramenta o agente deve escolher para cada pergunta.
 Ele recupera o esquema completo do banco de dados para o modelo.
Confira a resposta
40%
Construindo um Agente
Crie sua própria ferramenta de modelo Cypher
Esta lição foi útil?SimNão




Texto original
Return only relevant scalar properties — not whole nodes, relationships, paths, or embeddings
Avalie a tradução
O feedback vai ser usado para ajudar a melhorar o Google Tradutor  




Ferramentas para criação de modelos de cifra


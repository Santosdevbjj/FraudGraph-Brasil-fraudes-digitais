

Construindo Agentes no Neo4j Aura ›
Resumo do curso

Sérgio

Português (Brasil)
Powered by Google TradutorTradutor
Resumo do curso
Parabéns por concluir o módulo Building Agents no Neo4j Aura!

Esperamos que o curso tenha sido útil e que agora você se sinta mais confiante ao usar o Neo4j.

Se você gostou do curso, que tal compartilhar seu certificado com seus amigos e colegas? Vamos recapitular o que você aprendeu e destacar alguns pontos-chave.
Ver certificado
Adicionar ao LinkedIn
Parabéns por concluir o curso Aura Agent!

Você projetou, construiu e publicou um agente Neo4j Aura que responde a perguntas em linguagem natural usando seu grafo de conhecimento — e o conectou a um aplicativo de IA por meio do MCP.

Entendendo o Agente Aura
Agora você sabe como:

Entenda o que é o Aura Agent e quando usá-lo.

Explique como os agentes utilizam o raciocínio em múltiplas etapas para interpretar perguntas, selecionar ferramentas e gerar respostas.

Diferencie os três tipos de ferramentas: Modelo de Criptografia, Texto para Criptografia e Busca por Similaridade.

Habilite o Aura Agent nas configurações da sua organização e gerencie o acesso em nível de projeto.

Construindo um Agente
Agora você sabe como:

Crie um agente com IA a partir de um prompt e do seu esquema de instância.

Adicione ferramentas de modelo Cypher com parâmetros nomeados e tipados, além de descrições instrutivas.

Adicionar ferramentas Text2Cypher para perguntas ad-hoc onde a estrutura da consulta muda em tempo de execução.

Projete um agente com uma função, escopo e mapeamento de perguntas para ferramentas bem definidos.

Editar, excluir e gerenciar configurações de ferramentas e agentes.

Publicação e Conexão
Agora você sabe como:

Escolha entre os modos de acesso interno e externo.

Habilite o servidor MCP e exponha seu agente como uma ferramenta invocável para aplicações de IA.

Conecte seu agente ao Cursor usando o endpoint MCP e autentique-se através do Aura.

Teste seu agente no Cursor e verifique a seleção de ferramentas no painel de raciocínio.

Melhores práticas
Projeto
Mantenha os agentes focados em um único domínio. Um escopo restrito facilita a seleção de ferramentas para o LLM e produz resultados mais previsíveis.

Use modelos de código cifrado para qualquer questão em que você possa escrever o código cifrado completo agora, com apenas $parameterespaços para valores de variáveis. Reserve a conversão de texto para código cifrado para questões cuja estrutura se altera.

Atribua a cada padrão de questão distinto sua própria ferramenta. Uma ferramenta que abranja questões não relacionadas terá uma descrição vaga e será escolhida no momento errado.

Como escrever boas descrições
Escreva descrições de ferramentas que respondam a duas perguntas: o que esta ferramenta retorna e quando ela deve ser usada em vez das outras?

Escreva as descrições dos parâmetros como instruções com exemplos — "O ID do cliente, por exemplo, ALFKI ou QUICK" — e não apenas como rótulos.

Para o Text2Cypher, especifique quando usá-lo ("somente quando nenhuma outra ferramenta for adequada") e inclua o contexto específico do domínio, como rótulos de nós principais e tipos de relacionamento.

Testes e manutenção
Use o painel de raciocínio para verificar qual ferramenta o agente selecionou e qual Cypher foi gerado, especialmente para Text2Cypher.

Teste a saída do Text2Cypher antes de utilizá-la em produção. O código Cypher gerado pode variar entre as chamadas.

Após adicionar, editar ou excluir ferramentas, clique sempre em Atualizar agente para que a configuração seja mantida.

Quer saber mais?
Documentação do Aura Agent — Referência completa para ferramentas, publicação, modos de acesso e configuração do MCP

Especificação oficial do MCP — O padrão aberto por trás do recurso de servidor MCP do Aura

Tudo sobre MCP - Blog da Neo4j — Uma introdução ao MCP e como ele conecta aplicações de IA a fontes de dados.

Pronto para o seu próximo desafio?
Para aprofundar seus conhecimentos em IA generativa e Neo4j:

Fundamentos do Neo4j e GenAI - Compreenda os fundamentos da IA ​​generativa e como o Neo4j se integra a grandes modelos de linguagem.

Utilizando o Neo4j com o LangChain - Integre o Neo4j com o LangChain para criar pipelines e agentes de geração com recuperação aprimorada.

Introdução a índices vetoriais e dados não estruturados - Aprenda como gerar embeddings e construir índices vetoriais para busca por similaridade.

Para aprofundar o conhecimento sobre MCP e IA baseada em grafos:

Desenvolvimento com as ferramentas Neo4j MCP - Aprenda como conectar aplicações de IA às ferramentas e fontes de dados do Neo4j usando o Protocolo de Contexto de Modelo (MCP).

Criando ferramentas GraphRAG Python MCP - Crie seu próprio servidor GraphRAG MCP com ferramentas baseadas em grafos usando o SDK Python do MCP.

Criando ferramentas GraphRAG TypeScript para MCP - Desenvolva suas próprias ferramentas e servidor MCP usando o SDK TypeScript para MCP.

 

Ou por que não experimentar uma destas recomendações com base no seu histórico de matrículas?

Fundamentos do AuraDB
Aprenda a usar o Neo4j AuraDB, um serviço de banco de dados gráfico totalmente gerenciado na nuvem.

Ver curso →


Construindo Grafos de Conhecimento com Neo4j GraphRAG para Python
Aprenda a usar Python e LLMs para converter dados não estruturados em grafos de conhecimento.

Ver curso →






   

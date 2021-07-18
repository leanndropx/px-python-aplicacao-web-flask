# Este repositório contém: 



1. Uma aplicação web desenvolvida em Python com Flask. 
2. A aplicação conecta uma página HTML a um sistema em Python que acessa os endereços https://hn.algolia.com/api/v1/search_by_date?tags=story - notícias mais recentes - e https://hn.algolia.com/api/v1/search?tags=storyno - notícias mais populares; coleta seu conteúdo com dicionários JSON; converte-os para dicionários Python, para em seguida formatá-los e retorná-los como um output em uma página HTML personalizada.




#  Este repositório tem como finalidade:



2. Mostrar um pouco dos meus conhecimentos em flask, html, biblioteca requests e também trabalhar com conversão de arquivos JSON para Python.
3. contribuir com a comunidade compartilhando conhecimento prático, e também me abrir para aprendizados e contribuições.
3. Servir como meu material de apoio para relembrar conceitos, sintaxes, bibliotecas e funções de todos os recursos que foram usados para construir este projeto.



# Neste repositório foram usadas as bibliotecas:



1. requests

2. flask - com os módulos Flask, render_template e request 





# Para melhor explorá-lo, como principal sugestão, siga os passos abaixo:




1. Clone o repositório para o seu ambiente de desenvolvimento

2. Abra o terminal, caminhe até a pasta clonada do projeto. 

3. Na linha de comando, digite **pip3 install requests --users** para instalar a biblioteca Requests

4. Na linha de comando, digite **pip3 install flask --users** para instalar a biblioteca flask, que contém os módulos Flask, render_template e request que serão utilizados nesta aplicação.

   

Após a instalação de todas as bibliotecas necessárias, vamos a execução:



5. Na linha de comando, ainda dentro da pasta do projeto, digite **python3 main.py**

6. Pronto, o código será executado e.o framework flask iniciará um servidor local:

- Copie o endereço http do servidor que aparecerá em seu terminal
- Abra seu navegador e cole o endereço para acessar a aplicação. Você verá um header com o título do site e um menu logo abaixo com dois links: MOST POPULAR | MOST NEWS
- Ao clicar em MOST NEWS, a aplicação retorna as notícias mais recentes alimentadas no JSON coletado com requests
- Ao clicar em MOST POPULAR, a aplicação retorna as notícias mais populares. 
- Ao clicar no título de qualque notícia, a aplicação direciona uma nova página HTML que exibe todos os comentários - caso existam - feitos naquela notícia.



## **Como foram organizados os conteúdos** e por que:



O sistema é composto por 2 arquivos:

1. **main.py**: aqui está localizado o código principal, onde são importadas as bibliotecas utilizadas no programa - requests e flask - e onde foi estruturada as linhas de código para cada página HTML da aplicação.
2. **templates (diretório)**: este diretório é requisito do modo de trabalho com o framework flask, dentro dele estão localizadas as páginas HTML que serão renderizadas na aplicação. Para este projeto, são duas:
   - Index.html: página inicial, abre assim que o endereço da aplicação é acessado. 
   - id.html: página de uma notícias específica que exibe todos os comentários feitos, é acessada assim que o usuário clica no link da notícia. 

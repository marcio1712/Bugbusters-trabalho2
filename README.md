# Documentação do Projeto: Api-Spring 🎉

## Introdução
---
A documentação a seguir apresenta detalhes sobre o projeto de uma API de organização de eventos para a Sociedade Brasileira de Computação. A API foi desenvolvida em Java 11 utilizando o framework Spring Boot e permite o gerenciamento de usuários, eventos e edições.

## Endpoints 📡
---
A API disponibiliza os seguintes endpoints:

### Usuários 👤

- `GET {{urlbase}}/users`: Retorna a lista de usuários cadastrados.
- `POST {{urlbase}}/users`: Cria um novo usuário.
- `GET {{urlbase}}/users/{id}`: Retorna uma lista de eventos em que o usuário está com presença confirmado.

### Eventos 📅

- `GET {{urlbase}}/events`: Retorna a lista de eventos cadastrados.
- `POST {{urlbase}}/events`: Cria um novo evento.

### Edições 📅

- `GET {{urlbase}}/editions`: Retorna a lista de edições cadastradas.
- `POST {{urlbase}}/editions`: Cria uma nova edição de evento.

### Chaves 🔑

- `GET {{urlbase}}/keys`: Retorna a lista de chaves cadastradas.
- `POST {{urlbase}}/keys`: Cria uma nova chave de usuário.

### Tickets 🎟️

- `GET {{urlbase}}/tickets`: Retorna a lista de tickets cadastrados.
- `POST {{urlbase}}/tickets`: Cria um ticket para um evento.

### Avaliações 🌟

- `GET {{urlbase}}/editions`: Retorna a lista de avaliações realizadas.
- `POST {{urlbase}}/editions`: Cria uma nova avaliação para um evento.

## Configuração do Ambiente de Desenvolvimento 💻
---
Para configurar o ambiente de desenvolvimento e executar o projeto, siga as instruções abaixo:

1. Certifique-se de ter o JDK 11 instalado em seu sistema. Você pode fazer o download do JDK 17 em: [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)

2. Faça o download e instale uma IDE Java, como o IntelliJ IDEA. Você pode fazer o download do IntelliJ IDEA em: [https://www.jetbrains.com/idea/](https://www.jetbrains.com/idea/)

3. Clone este repositório em seu ambiente de desenvolvimento local.

4. Abra o projeto no IntelliJ IDEA.

5. Configure o JDK 17 nas configurações do projeto no IntelliJ IDEA.

6. Configure as dependências necessárias para o projeto, como o framework Spring Boot.

7. Configure o banco de dados MySQL 8 no arquivo `application.properties` localizado em `src/main/resources`. Altere as seguintes propriedades de acordo com a sua configuração:

> **Note**
> Recomendamos fortemente o uso do MySQL Workbench para facilitar o processo de configuração do projeto, uma documentação mais aprofundada para a configuração desta ferramenta pode ser encontrada [aqui](https://dev.mysql.com/doc/refman/8.0/en/).

> **Warning**
> O arquivo não será importado quando você realizar o clone do projeto, portanto o mesmo deverá ser criado no caminho indicado

```SQL
spring.datasource.url=jdbc:mysql://localhost/nome-do-banco
spring.datasource.username=usuario
spring.datasource.password=senha

spring.jpa.generate-ddl=true
spring.jpa.hibernate.ddl-auto=create

spring.jpa.show-sql=true
spring.jpa.properties.hibernate-dialect=org.hibernate.dialect.MySQL8Dialect

spring.mvc.pathmatch.matching-strategy = ANT_PATH_MATCHER
```

Certifique-se de substituir `nome-do-banco`, `usuario` e `senha` com as suas informações correspondentes.

8. Execute o projeto no IntelliJ IDEA.

## Executando os Testes Unitários 🧪
---
Este projeto utiliza testes unitários para garantir a qualidade e o bom funcionamento do sistema. Para executar os testes, siga as etapas abaixo:

1. Abra o IntelliJ IDEA.

2. Navegue até o pacote de testes do projeto.

3. Clique com o botão direito na pasta de testes e selecione "Run Tests".

## Testes Selenium 🐍
---
### Instruçõess e pré-requisitos para compilação e execução

* Pré-requisitos
	* [Python 3 na versão mais recente](https://www.python.org/download/releases/3.0/)
	* [Selenium](https://www.selenium.dev/downloads/)
		* Após a instalação, o arquivo do Selenium deve ser armazenado na pasta Bin do Python.
		> Instalação alternativa: ```python -m pip install selenium```
	* [Chrome Browser](https://www.google.com.br/chrome/)
		* Versão utilizada no projeto: 107.0.5304.18
	* [Google Chrome WebDriver](https://chromedriver.chromium.org/)
		* A versão do WebDriver deve ser compatível com a versão do Chrome, do contrário o sistema não funcionará. [Como encontrar a versão do seu Chrome](https://screencorp.zendesk.com/hc/pt-br/articles/115001590211-Visualizando-a-vers%C3%A3o-do-Google-Chrome)
		* Após a instalação, o arquivo do WebDriver deve ser armazenado na pasta Bin do Python.
		> Instalação alternativa: ```python -m pip install webdriver-manager```

* Para executar o projeto, basta executar o comando ```python index.py``` no terminal.

## CI/CD Pipeline ⚙️
---
Na pasta raiz do projeto existe um arquivo `Jenkinsfile` contendo o código fonte de uma pipeline CI/CD desenvolvida para o projeto que conta com os seguintes estágios.

Fez-se necessária a implementação dessa Pipeline a fim de obter-se uma maior produtividade ao desenvolver o sistema e garantir a qualidade e coesão do mesmo.

### Compilação ⚒️
Neste estágio é realizada a compilação do projeto utilizando o Maven.

### SonarQube 👁️‍🗨️
Este estágio é responsável pela execução do SonarQube, com objetivo de garantir as medidas de cobertura e qualidade de código, detectando possíveis *code smells* ao longo do desenvolvimento do projeto. 

### Selenium 🐍
Por fim, neste estágio é realizada a execução dos testes de requisitos funcionais, a fim de garantir que os mesmos sejam garantidos na medida do desenvolvimento do projeto.




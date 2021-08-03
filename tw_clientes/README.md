# Projeto fundamentos Django

## Sobre o projeto

Conteúdo didático para programadores iniciantes em django.\
este é um projeto de fundamentos, com ele iremos criar um crud de clientes.

## Criando um projeto com nome tw_clientes

Após ativar a virtualenv, iremos criar um novo projeto com o comando:

```bash
  django-admin startproject tw_clientes
```

## Criando aplicação clientes

```bash
  Python manage.py startpp clientes
```

## Iniciando projeto

```bash
  Python manage.py runserver
```

## Criando banco de dados

Autenticação

```bash
  systemctl start mariadb
```

No arquivo `Settings.py` precisamos modificar as configurações para mysql.\
Abrindo o terminal, precisamos criar o banco de dados.

```bash
  mysql -u root -p
```

após digitarmos a senha, iremos criar uma base de dados e verificar tabela:

```bash
  create database tw_django_fundamentos;
```

```bash
  use tw_django_fundamentos;
```

```bash
  show tables;
```

Criar tabelas no banco de dados

```bash
  Python manage.py migrate
```

### Mostrar tabelas do banco de dados:

```bash
  show tables;
```

| Tables_in_tw_django_fundamentos |     |     |
| :------------------------------ | :-- | :-- |
| `auth_group `                   |     |     |
| `auth_group_permissions`        |     |     |
| `auth_permission`               |     |     |
| `auth_user_groups`              |     |     |
| `auth_user_user_permissions`    |     |     |
| `django_admin_log`              |     |     |
| `django_content_type`           |     |     |
| `django_migrations`             |     |     |
| `django_session`                |     |     |

### modificar arquivo models.py

Dentro do arquivo `models.py` iremos criar uma classe para utilizar orm do django.

Dentro do arquivo `settings.py` iremos adicionar na tabela INSTALLED_APPS o nome `"clientes",`

Iremos migrar o model clientes

```bash
  Python manage.py makemigrations
```

Criar a tabela cliiente usando arquivo `0001_initial.py` dentro de makemigrations

aplicar a migração clientes, criando no banco de dados

```bash
  Python manage.py migrate
```

Mostrar tabelas do banco de dados:

```bash
  show tables;
```

| Tables_in_tw_django_fundamentos |            |     |
| :------------------------------ | :--------- | :-- |
| `auth_group `                   |            |     |
| `auth_group_permissions`        |            |     |
| `auth_permission`               |            |     |
| `auth_user_groups`              |            |     |
| `auth_user_user_permissions`    |            |     |
| `clientes_cliente`              | ADICIONADA |     |
| `django_admin_log`              |            |     |
| `django_content_type`           |            |     |
| `django_migrations`             |            |     |
| `django_session`                |            |     |

É possível exibir todos os campos definidos com:

```bash
  desc clientes_cliente;
```

### Views

A camada View é responsável por tramitar as informações obtidas pelo model e exibi-las ao usuário (seja através de
um template ou não)

### urls

As rotas são de fundamental importância para que o usuário consiga executar determinada funcionalidade do
sistema. No Django, cada rota é responsável por executar um método na view da aplicação, que exibe alguma
informação para o usuário.\
No Django, o processamento de rotas acontece da seguinte forma:

- 1 - Uma URL é invocada por meio do navegador;
- 2 - O Django captura a URL, verifica o método que esta rota executa e repassa a requisição para ela;
- 3 - A partir daí o restante da requisição é feita pelas outras camadas do Django.

### Templates

- criar template e renderizar para o nosso banco de dados
  criar um arquivo com nome: `clientes/lista_clientes.html`

- criar uma tabela:

| Lista de Clientes    |     |     |
| :------------------- | :-- | :-- |
| `Nome `              |     |     |
| `Data de Nascimento` |     |     |
| `Sexo`               |     |     |

### Adicionando clientes direto no banco mysql

```bash
  systemctl start mariadb
```

```bash
  mysql -u root -p
```

```bash
  use tw_django_fundamentos;
```

```bash
  desc clientes_cliente;
```

```bash
  INSERT INTO clientes_cliente (nome, data_nascimento, email, sexo) VALUES ("João", '1990-01-01', "joao@gmail.com", "M")
```

- [listar clientes](http://127.0.0.1:8000/clientes/listar)

- A rota listar, chama o método lista_clientes e o método obtem todos os clientes do banco de dados e salva na variável clientes.
- Assim, ele retorna renderizando nosso html e envia a variável de cliente.
- O template com essas informações, cria um for e vai iterar sobre a lista dos clientes do banco de dados.
  Em resumo: começa chamando a rota, chamar a view, obtem dados no banco de dados, retornar esses dados para o template e renderizar todas as informações.

- inserir mais um nome no banco de dados:

```bash
  INSERT INTO clientes_cliente (nome, data_nascimento, email, sexo) VALUES ("Maria", '1989-02-01', "maria@mail.com", "F");
```

- podemos visualizar:

```bash
  select * from clientes_cliente;
```

### forms

Dentro do diretório clientes, criar arquivo `forms.py`

- importar forms e importar Cliente
- criar uma classeModelForm
  Dentro do diretório templates / clientes, criar um arquivo `form_cliente.html`

ao criarmos um arquivo HTML, podemos utilizar apenas uma linha
para criar um formulário `<body>{{ form.as_p }}</body`

- Porém, nós iremos renderizar criando um formulário manualmente.
  nome, sexo, data de nascimento, email e profissão.

- criar a tag form e um csrf_token, uma nova div para submeter as informações do formulário no arquivo `form_cliente.html`

### bootstrap

- criando href dentro do arquivo `lista_clientes.html` adicionar href com bootstrapcdn
- Dentro da tag body, incluir uma nova classe table `class="table"`
- criando button com classe btn, redirecionando para rota de cadastrar cliente dentro de `urls.py`
- criando também href dentro do arquivo `form_clientes.html` adicionar href com bootstrapcdn

### base Templates

- criando um arquivo `base.html` com as informações dos arquivo `lista_clientes.html` e `form_clientes.html`
- cirando arquivos estáticos. criar diretórios dentro de `clientes` e criar `static / clientes / css` criar um arquivo `style.css`
- dentro do arquivo `base.html` incluir `href="{% {% static 'clientes/css/style.css' %} %`

### Filtros

- dentro do diretório `clientes` criar diretório e `templatetags / meusfiltros.py `
  adicionar Filtros

```bash
from django import template

register = template.Library()


@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})
```

- tradução da informação
  dentro do arquivo `settings.py` modificar: LANGUAGE_CODE = 'pt-br' e TIME_ZONE = 'America/Sao_Paulo'

### Buscar Cliente por id

- buscar na nossa tabela de cliente o id e renderizando um template
  adicionar uma função id dentro do arquivo `views.py`e adiconar um path dentro de `urls.py`

- criar template dentro do diretório `template/clientes` com nome `lista_cliente`

```bash
{% extends 'clientes/base.html' %} {% block titulo %} Listagem de cliente {%
endblock titulo %} {% block conteúdo %}
<div class="card">
  <div class="card-header">Dados do cliente</div>

  <div>
    <h5 class="card-title">Nome: {{cliente.nome}}</h5>
    <h5 class="card-title">Sexo: {{cliente.sexo}}</h5>
    <h5 class="card-title">Data de Nascimento: {{cliente.data_nascimento}}</h5>
    <h5 class="card-title">Email: {{cliente.email}}</h5>
    <h5 class="card-title">Prof: {{}}</h5>
  </div>
</div>
```

### editar cliente

- criar uma função no arquivo `views.py` para editar o cliente
- criar uma rota no arquivo `urls.py` e passar o id do cliente
- criar um novo item com nome de Ações e um link para editar e remover dentro do arquivo `lista_clientes.html`
  editar

### excluir cliente

- criar uma função dentro do diretório `views.py` remover_cliente
- criar um template com nome `confirma_exclusao.html` dentro do diretório `templates/clientes`
- criar uma rota responsável para remover dentro do diretório `urls.py` e uma href responsável pela rota remover_cliente dentro do arquivo `lista_clientes.html`

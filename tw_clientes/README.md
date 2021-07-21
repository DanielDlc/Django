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

## modificar arquivo models.py

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

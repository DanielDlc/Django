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

# Django

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/DanielDlc/Django/blob/main/LICENSE)

### Criando uma virtualenv

abra o seu terminal e digite:

```bash
python -m venv my_env
```

ativando virtualenv no windows:

```bash
.\my_env\Scripts\activate
```

### Django

instalando django 3 (observe se sua virtualenv está ativada!)

```bash
pip install "Django==3.0.*"
```

Criando o primeiro projeto Django:

```bash
django-admin startproject mysite
```

Efetuando as migrações:

```bash
python manage.py migrate
```

testar o projeto:

```bash
python manage.py runserver
```

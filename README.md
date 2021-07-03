# Django

## Tutorial para instalação e configuração usando Arch linux bspwm

Inicialmente, abra o seu `terminal` com `super+enter` e digite os seguintes comandos, para instalar a `virtualenv` fornece suporte para a criação de “ambientes virtuais” no *Python*:
```bash
pip install virtualenv
```

podemos verificar se o `virtualenv` está em nosso `PATH` digitando:
```bash
virtualenv
```

caso não encontre o comando virtualenv, podemos adiconar ao `PATH` adicionando a seguinte linha no diretório\
`vim .bashrc`\
ou\
`vim .zshrc`
```bash
export PATH="${PATH}:/home/substitua_pelo_nome_do_seu_usuário/.local/bin"
```\


para criar uma virtualenv, podemos simplismente digitar: `virtualenv` e_um_nome_de_uma_venv, no meu caso irei criar com nome `django`
```bash
virtualenv django
```

para ativar a `virtualenv` considerando que você esteja no diretório home e sua virtualenv tenha sido criada no mesmo diretório
```bash
source django/bin/activate
```
para desativar a `virtualenv`:
```bash
deactivate
```\


## Instalação do Django
após ativar sua `virtualenv`, podemos acessar o diretório django]e instalar o django com:
```bash
pip install django
```

podemos confirmar se o [django] foi instalado corretamente! digitando,`python` ou `python3` no [shell] e após chamar o interpretador do python:
```bash
import django

django.get_version()
```


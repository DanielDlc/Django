# Django

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/DanielDlc/Django/blob/main/LICENSE)

## Sobre o projeto
Conteúdo didático para programadores iniciantes em django.\
O conteúdo abaixo, contém um pequeno tutorial com o guia de instalação do django e a configuração de uma virtualenv.\
Nesse tutorial foi utilizado um SO Arch linux bspwm.

### Inicialmente iremos instalar o virtualenv para a criação de “ambientes virtuais” utilizado em Python
abra o seu terminal e digite:
```bash 
pip install virtualenv
```

podemos verificar se o virtualenv está em nosso PATH digitando:
```bash
virtualenv
```

caso não encontre o comando virtualenv, podemos definir a variável PATH dentro do diretório\
`vim .bashrc`
```bash
export PATH="${PATH}:/home/substitua_pelo_nome_do_seu_usuário/.local/bin"
```


para criar uma virtualenv, podemos digitar virtualenv venv ou um nome de sua preferência! no meu caso, irei criar com o nome:
```bash
virtualenv django
```
### ativando e desativando o virtualenv

Ativando virtualenv:
```bash
source django/bin/activate
```

Desativando virtualenv:
```bash
deactivate
```


## Instalação do Django
após ativar sua virtualenv, iremos instalar o django. Assim teremos um ambiente completamente isolado.
```bash
pip install django
```

para confirmar se o django foi instalado e está funcionando corretamente\
podemos utilizar o shell interativo digitando: `python -i`
```bash
import django

django.get_version()
```


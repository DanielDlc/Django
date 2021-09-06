from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    nome_da_empresa = "DLC Tecnologia"
    descricao_da_empresa = "Empresa atualizada em novas tecnologias com mais de 2 anos de experiência em desenvolvimento de software para pequenas e médias empresas, "\
        "incluindo criação de Sites, Portfólio, Manutenção de computadores e remoção de malwares. "\
        "Com vasto conhecimento em: Engenharia da Computação, Microservices, Serverless, Design System e outras práticas."
    contato_empresa = {
        "endereco": "Rua visconde de pirajá - Ipanema - Rio de Janeiro - RJ",
        "telefone": "21-999183939",
        "email": "dlc.engcomputacao@gmail.com"
    }

    cursos_home = {
        "1": {"titulo": "Django ", "descricao": "Aprenda todo posicionamento no Google.!!"},
        "2": {"titulo": "Flask ", "descricao": "Aprenda toda a base do FFlask Agora mesmo!!"},
        "3": {"titulo": "Estrutura de dados", "descricao": "Aprenda Estrutura de dados Agora mesmo!!"}
    }

    return render(request, 'empresa/index.html', {'nome_empresa': nome_da_empresa, 'descricao_empresa': descricao_da_empresa,
                                                  'contato_empresa': contato_empresa, 'cursos_home': cursos_home})


def about(request):
    return HttpResponse("Página sobre")


def contact(request, id):
    return HttpResponse(id)

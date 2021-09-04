from django.shortcuts import render

# Create your views here.


def index(request):
    nome_da_empresa = "DLC Tecnologia"
    descricao_da_emrpesa = "Empresa atualizada em novas tecnologias com mais de 2 anos de experiência em desenvolvimento de software para pequenas e médias empresas, "\
        "incluindo criação de Sites, Portfólio, Manutenção de computadores e remoção de malwares. "\
        "Com vasto conhecimento em: Engenharia da Computação, Microservices, Serverless, Design System e outras práticas."
    contato_empresa = {
        "endereco": "Rua visconde de pirajá - Ipanema - Rio de Janeiro - RJ",
        "telefone": "21-999183939",
        "email": "dlc.engcomputacao@gmail.com"
    }
    return render(request, 'empresa/index.html', {'nome_empresa': nome_da_empresa, 'descricao_empresa': descricao_da_emrpesa, 'contato_empresa': contato_empresa})

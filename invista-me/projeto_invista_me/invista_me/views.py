from django.shortcuts import render
from django.shortcuts import HttpResponse


def pagina_inicial(request):
    return HttpResponse("Pronto para investir! Daniel.")


def novo_investimento(request):
    return render(request, "investimentos/novo_investimento.html")


def investimento_registrado(request):
    print(request.POST.get("TipoInvestimento"))
    investimento = {" tipo_investimento": request.POST.get("TipoInvestimento")}
    return render(request, "investimentos/investimento_registrado.html", investimento)

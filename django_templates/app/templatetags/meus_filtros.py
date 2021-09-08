from django import template

register = template.Library()


@register.filter(name='remover_letra')
def remover_letra(var, letra):
    return var.replace(letra, '')
# DLCTecnologia

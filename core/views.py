from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def index(request):
    context = {
        'nome_pagina': 'Página Inicial'
    }

    return render(request, 'index.html', context)


def catalogo(request):
    context = {
        'nome_pagina': 'Catálogo'
    }

    return render(request, 'catalogo.html', context)


def contato(request):
    context = {
        'nome_pagina': 'Fale Conosco'
    }

    return render(request, 'contato.html', context)
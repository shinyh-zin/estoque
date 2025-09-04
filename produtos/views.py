from django.shortcuts import render

# Create your views here.
from .models import Produtos
def lista_produtos(request):
    Produtos = Produtos.objects.all()
    return render(request, 'produtos/lista.html', {'produtos':Produtos})
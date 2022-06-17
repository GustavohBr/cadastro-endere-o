from django.shortcuts import render
from enderecos.forms import Cadastro
from enderecos.models import Enderecos

def end_cadastrados(request):
    lista_end = Enderecos.objects.all()
    context = {
        'lista_end': lista_end
    }
    return render(request, 'enderecos/main.html', context=context)

def form_cad(request):
    if request.method == "GET":
        form = Cadastro()
        context = {
            'form': form
        }
        return render(request, 'enderecos/cadastro.html', context=context)
    else:

        form = Cadastro(request.POST)
        if form.is_valid():
            end = form.save()
            form = Cadastro()
        
        context = {
        'form': form
        }
        return render(request, 'enderecos/cadastro.html', context=context)

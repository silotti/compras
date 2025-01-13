from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView
from .models import Item
from .forms import ItemForm

class ListaComprasView(ListView):
    model = Item
    template_name = 'lista_compras/lista.html'
    context_object_name = 'itens'

def adicionar_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_compras:lista_compras')
    else:
        form = ItemForm()
    
    return render(request, 'lista_compras/form.html', {'form': form})

def editar_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('lista_compras:lista_compras')
    else:
        form = ItemForm(instance=item)
    
    return render(request, 'lista_compras/form.html', {'form': form})

def marcar_comprado(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.comprado = not item.comprado
    item.save()
    return redirect('lista_compras:lista_compras')

def aumentar_quantidade(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.quantidade += 1
    item.save()
    return redirect('lista_compras:lista_compras')

def diminuir_quantidade(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    return redirect('lista_compras:lista_compras')

def excluir_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('lista_compras:lista_compras')

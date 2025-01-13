from django.urls import path
from . import views

app_name = 'lista_compras'

urlpatterns = [
    path('', views.ListaComprasView.as_view(), name='lista_compras'),
    path('adicionar/', views.adicionar_item, name='adicionar_item'),
    path('editar/<int:pk>/', views.editar_item, name='editar_item'),
    path('marcar/<int:pk>/', views.marcar_comprado, name='marcar_comprado'),
    path('aumentar/<int:pk>/', views.aumentar_quantidade, name='aumentar_quantidade'),
    path('diminuir/<int:pk>/', views.diminuir_quantidade, name='diminuir_quantidade'),
    path('excluir/<int:pk>/', views.excluir_item, name='excluir_item'),
]

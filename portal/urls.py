from django.urls import path
from portal import views

urlpatterns = [

    path('', views.home, name='home'),
    path('familia/add/', views.familia_add, name='familia_add'),
    path('lista/responsavel/', views.lista_responsavel, name='lista_responsavel'),
    path('lista/dependente/', views.lista_dependente, name='lista_dependente'),
    path('lista/cuidador/', views.lista_cuidador, name='lista_cuidador'),
    path('responsavel/add/', views.responsavel_add, name='responsavel_add'),
    path('dependente/add/', views.dependente_add, name='dependente_add'),
    path('cuidador/add/', views.cuidador_add, name='cuidador_add'),

]

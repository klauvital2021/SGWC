from django.urls import path
from portal import views

#app_name = "portal"

urlpatterns = [

    path('', views.HomePageView.as_view(), name='home'),
    path('familia/add/', views.familia_add, name='familia'),
    path('lista/responsavel/', views.lista_responsavel, name='responsaveis'),
    path('lista/dependente/', views.lista_dependente, name='dependentes'),
    path('lista/cuidador/', views.lista_cuidador, name='cuidadores'),
    path('responsavel/add/', views.responsavel_add, name='responsavel_add'),
    path('dependente/add/', views.dependente_add, name='dependente_add'),
    path('cuidador/add/', views.cuidador_add, name='cuidador_add'),

]

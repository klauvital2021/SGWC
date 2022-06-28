from django.urls import path
from portal import views
from django.views.generic.base import RedirectView


#app_name = "portal"

urlpatterns = [

    path('', views.HomePageView.as_view(), name='home'),
    path('login/familia/', views.login_familia, name='login_familia'),
    path('validar_login/', views.validar_login, name='validar_login'),
    path('sair/familia/', views.sair_familia, name='sair'),

    path('dependente/', views.lista_dependente, name='dependentes'),
    path('dependente/add/', views.dependente_add, name='dependente_add'),
    path('dependente/edit/<int:dependente_pk>/', views.dependente_edit, name='dependente_edit'),
    path('dependente/delete/<int:dependente_pk>/', views.dependente_delete, name='dependente_delete'),

    path('familia/', views.lista_familia, name='familia'),
    path('familia/add/', views.familia_add, name='familia_add'),
    path('familia/edit/<int:familia_pk>/', views.familia_edit, name='familia_edit'),
    path('familia/delete/<int:familia_pk>/', views.familia_delete, name='familia_delete'),

    path('responsavel/', views.lista_responsavel, name='responsaveis'),
    path('responsavel/add/', views.responsavel_add, name='responsavel_add'),
    path('responsavel/edit/<int:responsavel_pk>/', views.responsavel_edit, name='responsavel_edit'),
    path('responsavel/delete/<int:responsavel_pk>/', views.responsavel_delete, name='responsavel_delete'),

    path('cuidador/', views.lista_cuidador, name='cuidadores'),
    path('cuidador/add/', views.cuidador_add, name='cuidador_add'),

]

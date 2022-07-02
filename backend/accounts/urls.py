from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from backend.accounts import views as v

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),  # noqa E501
    path('logout', LogoutView.as_view(), name='logout'),  # noqa E501
    path('responsavel/principal/add/', v.responsavel_principal_add, name='responsavel_principal_add'),   # noqa E501
]

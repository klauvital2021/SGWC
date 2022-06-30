from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import Responsavel, Dependente, Cuidador, Familia
from .forms import UserChangeForm, UserCreationForm, FamiliaForm


admin.site.register(Familia)
admin.site.register(Responsavel)
admin.site.register(Cuidador)
admin.site.register(Dependente)



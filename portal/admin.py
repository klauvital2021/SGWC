from django.contrib import admin
from .models import Responsavel, Dependente, Cuidador, Familia

admin.site.register(Responsavel)
admin.site.register(Cuidador)
admin.site.register(Dependente)
admin.site.register(Familia)


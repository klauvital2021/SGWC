from django.contrib import admin

from .models import Cuidador, Dependente, Familia, Responsavel


@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'data_inicio',
        'data_fim',
    )
    # list_display_links = ('dependente',)
    search_fields = (
        'usuario__user__first_name',
        'usuario__user__last_name',
        'usuario__user__email',
    )
    # list_filter = ('type',)
    # date_hierarchy = 'created'


@admin.register(Dependente)
class DependenteAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'rg',
        'cpf',
    )
    # list_display_links = ('dependente',)
    search_fields = (
        'usuario__user__first_name',
        'usuario__user__last_name',
        'usuario__user__email',
    )
    # list_filter = ('type',)
    # date_hierarchy = 'created'


@admin.register(Familia)
class FamiliaAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
    )
    # list_display_links = ('dependente',)
    search_fields = (
        'nome',
        'usuario__user__first_name',
        'usuario__user__last_name',
        'usuario__user__email',
    )
    # list_filter = ('type',)
    # date_hierarchy = 'created'


@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'rg',
        'cpf',
    )
    # list_display_links = ('dependente',)
    search_fields = (
        'usuario__user__first_name',
        'usuario__user__last_name',
        'usuario__user__email',
    )
    # list_filter = ('type',)
    # date_hierarchy = 'created'

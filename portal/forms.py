import requests
from django import forms
from django.forms import PasswordInput
from portal.models import Responsavel, Dependente, Cuidador,Familia
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm


civil_choices = (
    ('1', 'Solteiro(a)'),
    ('2', 'Casado(a)'),
    ('3', 'Divorciado(a)'),
    ('4', 'Viuvo(a)'),
    ('5', 'União Estável'),
    ('6', 'Outros'),
    )

regime_choices = (
    ('1', 'CLT'),
    ('2', 'PJ'),
    ('3', 'Free Lance'),
    ('4', 'Prestação Serviços'),
    )

turno_choices = (
    ('1', 'Diurno'),
    ('2', 'Noturno'),
    )

parentesco_choices = (
    ('1', 'Filho'),
    ('2', 'Neto'),
    ('3', 'Irmão'),
    ('4', 'Outro'),

)

tipo_usuario_choices = (
    ('1', 'Administrador'),
    ('2', 'Responsável'),
    ('3', 'Cuidador'),
    ('4', 'Dependente'),
    ('5', 'Técnico em Enfermagem')

    )


class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = [
            'username',
            'nome',
            'endereco',
            'bairro',
            'cidade',
            'uf',
            'email',
            'password',
            'status'
        ]
        exclude = ['username']
        widgets = {
            'password': forms.PasswordInput(),

        }


class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = '__all__'
        #exclude = ('familia',)

        widgets = {
            'senha': forms.PasswordInput(),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dtanasc'].widget.attrs.update({'class': 'mask-date'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})



class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dtanasc'].widget.attrs.update({'class': 'mask-date'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})


class CuidadorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dtanasc'].widget.attrs.update({'class': 'mask-date'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
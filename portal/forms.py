import requests
from django import forms
from django.forms import PasswordInput
from portal.models import Responsavel, Dependente, Cuidador,Familia, Consultas, Medicamentos, Pos_Consultas
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.middleware import SessionMiddleware


civil_choices = (
    ('1', 'Solteiro(a)'),
    ('2', 'Casado(a)'),
    ('3', 'Divorciado(a)'),
    ('4', 'Viuvo(a)'),
    ('5', 'União Estável'),
    ('6', 'Outros'),
    )

regime_choices = (
    ('CLT', 'CLT'),
    ('PJ', 'PJ'),
    ('FREE', 'Free Lance'),
    ('PS', 'Prestação Serviços'),
    )

turno_choices = (
    ('D', 'Diurno'),
    ('N', 'Noturno'),
    )

parentesco_choices = (
    ('F', 'Filho'),
    ('N', 'Neto'),
    ('I', 'Irmão'),
    ('O', 'Outro'),

)


class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = [
            'nome',
            'endereco',
            'bairro',
            'cidade',
            'uf',
            'email',
            'senha',
            'status'
        ]
        widgets = {
            'senha': forms.PasswordInput(),
        }


class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = [
            'familia',
            'parentesco',
            'nome',
            'dtanasc',
            'cpf',
            'cidade',
            'celular_whatsapp',
            'email',
            'senha',
        ]
        exclude = ('status','nacionalidade','naturalidade', 'estado_civil','bairro', 'endereco','uf', 'nome_conjuge', 'rg')

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
        fields = [
            'familia',
            'nome',
            'dtanasc',
            'estado_civil',
            'nome_conjuge',
            'cpf',
            'cidade',
            'celular_recado',
            'convenio_medico',
            'contato_fone_convenio',
            'status',
        ]
        exclude = ('nacionalidade', 'naturalidade', 'senha', 'bairro', 'endereco', 'uf', 'rg')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dtanasc'].widget.attrs.update({'class': 'mask-date'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})


class CuidadorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = '__all__'
        #exclude = ('nacionalidade', 'naturalidade', 'bairro', 'endereco', 'uf')

        widgets = {
                'senha': forms.PasswordInput(),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dtanasc'].widget.attrs.update({'class': 'mask-date'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['data_inicio'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_fim'].widget.attrs.update({'class': 'mask-date'})



class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = '__all__'

        widgets = {

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_consulta'].widget.attrs.update({'class': 'mask-date'})
        self.fields['hora'].widget.attrs.update({'class': 'mask-cpf'})


class PosConsultaForm(forms.ModelForm):
    class Meta:
        model = Pos_Consultas
        fields = '__all__'

class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamentos
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_inicio'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_fim'].widget.attrs.update({'class': 'mask-date'})
        self.fields['hora'].widget.attrs.update({'class': 'mask-hora'})


from django import forms

from .models import Cuidador, Dependente, Familia, Responsavel


class FamiliaForm(forms.ModelForm):

    class Meta:
        model = Familia
        fields = (
            'nome',
            'endereco',
            'bairro',
            'cidade',
            'uf',
        )


class ResponsavelForm(forms.ModelForm):

    class Meta:
        model = Responsavel
        fields = (
            'data_nascimento',
            'rg',
            'cpf',
            'celular_whatsapp',
            'parentesco_do_responsavel',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})


class CuidadorForm(forms.ModelForm):

    class Meta:
        model = Cuidador
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})
        self.fields['data_inicio'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_fim'].widget.attrs.update({'class': 'mask-date'})


class DependenteForm(forms.ModelForm):

    class Meta:
        model = Dependente
        fields = [
            'familia',
            'data_nascimento',
            'rg',
            'cpf',
            'celular_whatsapp',
            'celular_recado',
            'estado_civil',
            'nome_conjuge',
            'nacionalidade',
            'parentesco_do_responsavel',
            'dependente_convenio_medico',
            'dependente_contato_fone_convenio',
            'dependente_contato_endereco_convenio',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_nascimento'].widget.attrs.update({'class': 'mask-date'})  # noqa E501
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})

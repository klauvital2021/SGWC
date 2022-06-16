from django import forms
from portal.models import Responsavel, Dependente, Cuidador,Familia, Usuario


status_choices = (
        ('1', 'Ativo'),
        ('2', 'Inativo')
    )

class FamiliaForm(forms.ModelForm):
    class Meta:
        model = Familia
        fields = '__all__'


class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dtanasc'].widget.attrs.update({'class': 'mask-date'})
        self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


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
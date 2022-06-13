from django import forms
from portal.models import Responsavel, Dependente, Cuidador,Familia


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
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class DependenteForm(forms.ModelForm):
    class Meta:
        model = Dependente
        fields = '__all__'


class CuidadorForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = '__all__'

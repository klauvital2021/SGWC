from django import forms

from .models import Consulta, Medicamento, PosConsulta


class ConsultaForm(forms.ModelForm):

    class Meta:
        model = Consulta
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_consulta'].widget.attrs.update({'class': 'mask-date'})   # noqa E501
        self.fields['hora'].widget.attrs.update({'class': 'mask-hora'})

class PosConsultaForm(forms.ModelForm):

    class Meta:
        model = PosConsulta
        fields = '__all__'


class MedicamentoForm(forms.ModelForm):

    class Meta:
        model = Medicamento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['data_inicio'].widget.attrs.update({'class': 'mask-date'})
        self.fields['data_fim'].widget.attrs.update({'class': 'mask-date'})
        self.fields['hora'].widget.attrs.update({'class': 'mask-hora'})

from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ConsultaForm, MedicamentoForm, PosConsultaForm
from .models import Consulta, Medicamento, PosConsulta


class ConsultaListView(ListView):
    model = Consulta


class ConsultaDetailView(DetailView):
    model = Consulta


class ConsultaCreateView(CreateView):
    model = Consulta
    form_class = ConsultaForm


class ConsultaUpdateView(UpdateView):
    model = Consulta
    form_class = ConsultaForm


def consulta_delete(request):
    ...


class PosConsultaListView(ListView):
    model = PosConsulta


class PosConsultaDetailView(DetailView):
    model = PosConsulta


class PosConsultaCreateView(CreateView):
    model = PosConsulta
    form_class = PosConsultaForm


class PosConsultaUpdateView(UpdateView):
    model = PosConsulta
    form_class = PosConsultaForm


def posconsulta_delete(request):
    ...


class MedicamentoListView(ListView):
    model = Medicamento


class MedicamentoDetailView(DetailView):
    model = Medicamento


class MedicamentoCreateView(CreateView):
    model = Medicamento
    form_class = MedicamentoForm


class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    form_class = MedicamentoForm


def medicamento_delete(request):
    ...

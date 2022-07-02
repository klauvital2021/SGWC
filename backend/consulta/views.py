from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ConsultaForm, MedicamentoForm, PosConsultaForm
from .models import Consulta, Medicamento, PosConsulta


class ConsultaListView(LRM, ListView):
    model = Consulta


class ConsultaDetailView(LRM, DetailView):
    model = Consulta


class ConsultaCreateView(LRM, CreateView):
    model = Consulta
    form_class = ConsultaForm


class ConsultaUpdateView(LRM, UpdateView):
    model = Consulta
    form_class = ConsultaForm


def consulta_delete(request):
    ...


class PosConsultaListView(LRM, ListView):
    model = PosConsulta


class PosConsultaDetailView(LRM, DetailView):
    model = PosConsulta


class PosConsultaCreateView(LRM, CreateView):
    model = PosConsulta
    form_class = PosConsultaForm


class PosConsultaUpdateView(LRM, UpdateView):
    model = PosConsulta
    form_class = PosConsultaForm


def posconsulta_delete(request):
    ...


class MedicamentoListView(LRM, ListView):
    model = Medicamento


class MedicamentoDetailView(LRM, DetailView):
    model = Medicamento


class MedicamentoCreateView(LRM, CreateView):
    model = Medicamento
    form_class = MedicamentoForm


class MedicamentoUpdateView(LRM, UpdateView):
    model = Medicamento
    form_class = MedicamentoForm


def medicamento_delete(request):
    ...

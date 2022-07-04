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


'''
    def form_valid(self, form):
        # Cria o User.
        user = user_create(form)

        self.object = form.save(commit=False)

        # Associa o User ao Dependente
        self.object.user = user

        # Adiciona o Dependente ao grupo 'dependente'.
        add_to_group_consulta(form, user)

        # Associa a Familia.
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        self.object.familia = familia
        self.object.save()

        return super().form_valid(form)
'''


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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


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

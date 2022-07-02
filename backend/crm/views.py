from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CuidadorForm, DependenteForm, FamiliaForm, ResponsavelForm
from .models import Cuidador, Dependente, Familia, Responsavel


class DependenteListView(LRM, ListView):
    model = Dependente


class DependenteDetailView(LRM, DetailView):
    model = Dependente


class DependenteCreateView(LRM, CreateView):
    model = Dependente
    form_class = DependenteForm


class DependenteUpdateView(LRM, UpdateView):
    model = Dependente
    form_class = DependenteForm


def dependente_delete(request):
    ...


class FamiliaListView(LRM, ListView):
    model = Familia

    def get_queryset(self):
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        queryset = Familia.objects.filter(nome=familia)
        return queryset


class FamiliaDetailView(LRM, DetailView):
    model = Familia


class FamiliaCreateView(LRM, CreateView):
    model = Familia
    form_class = FamiliaForm

    def form_valid(self, form):
        # Pega o objeto Responsavel.
        user = self.request.user
        responsavel = Responsavel.objects.get(user=user)

        self.object = form.save()

        # Associa o Responsavel a Família.
        responsavel.familia = self.object
        responsavel.save()
        return super().form_valid(form)


class FamiliaUpdateView(LRM, UpdateView):
    model = Familia
    form_class = FamiliaForm


def familia_delete(request):
    ...


class ResponsavelListView(LRM, ListView):
    model = Responsavel

    def get_queryset(self):
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        queryset = Responsavel.objects.filter(familia__nome=familia)
        return queryset


class ResponsavelDetailView(LRM, DetailView):
    model = Responsavel


class ResponsavelCreateView(LRM, CreateView):
    model = Responsavel
    form_class = ResponsavelForm


class ResponsavelUpdateView(LRM, UpdateView):
    model = Responsavel
    form_class = ResponsavelForm


def responsavel_delete(request):
    ...


class CuidadorListView(LRM, ListView):
    model = Cuidador


class CuidadorDetailView(LRM, DetailView):
    model = Cuidador


class CuidadorCreateView(LRM, CreateView):
    model = Cuidador
    form_class = CuidadorForm


class CuidadorUpdateView(LRM, UpdateView):
    model = Cuidador
    form_class = CuidadorForm


def cuidador_delete(request):
    ...

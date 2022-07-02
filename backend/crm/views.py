from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import CuidadorForm, DependenteForm, FamiliaForm, ResponsavelForm
from .models import Cuidador, Dependente, Familia, Responsavel


class DependenteListView(ListView):
    model = Dependente


class DependenteDetailView(DetailView):
    model = Dependente


class DependenteCreateView(CreateView):
    model = Dependente
    form_class = DependenteForm


class DependenteUpdateView(UpdateView):
    model = Dependente
    form_class = DependenteForm


def dependente_delete(request):
    ...


class FamiliaListView(ListView):
    model = Familia

    def get_queryset(self):
        usuario = self.request.user.usuarios.first()
        familia = usuario.familia
        queryset = Familia.objects.filter(nome=familia)
        return queryset


class FamiliaDetailView(DetailView):
    model = Familia


class FamiliaCreateView(CreateView):
    model = Familia
    form_class = FamiliaForm


class FamiliaUpdateView(UpdateView):
    model = Familia
    form_class = FamiliaForm


def familia_delete(request):
    ...


class ResponsavelListView(ListView):
    model = Responsavel


class ResponsavelDetailView(DetailView):
    model = Responsavel


class ResponsavelCreateView(CreateView):
    model = Responsavel
    form_class = ResponsavelForm


class ResponsavelUpdateView(UpdateView):
    model = Responsavel
    form_class = ResponsavelForm


def responsavel_delete(request):
    ...


class CuidadorListView(ListView):
    model = Cuidador


class CuidadorDetailView(DetailView):
    model = Cuidador


class CuidadorCreateView(CreateView):
    model = Cuidador
    form_class = CuidadorForm


class CuidadorUpdateView(UpdateView):
    model = Cuidador
    form_class = CuidadorForm


def cuidador_delete(request):
    ...


def cadastrar_usuario(request):
    form = FamiliaForm(request.POST or None)
    if request.POST:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(
            # Truque para transformar username em email.
            username=email,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
        )

        if form.is_valid():
            '''
            Solução para colocar mais de um usuário na mesma família.
            '''
            try:
                nome = form.data.get('nome')
                familia = Familia.objects.get(nome=nome)
                print('existe')
            except Familia.DoesNotExist:
                familia = form.save()
                print('novo')
            except Exception as e:
                raise e
            familia.user = user
            familia.save()
            return redirect(reverse_lazy('home'))

    context = {
        'form': form,

    }
    return render(request, 'portal/familia_add.html', context)

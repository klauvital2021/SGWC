from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.db.models import Q
from hashlib import sha256
from django.contrib.auth.decorators import login_required
from portal.forms import ResponsavelForm, CuidadorForm, DependenteForm, FamiliaForm
from portal.models import Responsavel, Cuidador, Dependente, Familia, Usuario



class HomePageView(TemplateView):
     template_name = "portal/home.html"


def home(request):
     if request.session.get('logado'):
          return render(request, 'portal/home.html')
     else:
          return redirect('/login/familia/?status=2')


def login_familia(request):
     status = request.GET.get('status')
     return render(request, 'portal/login_familia.html', {'status': status})


def validar_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    #senha = sha256(senha.enconde()).hexdigest()

    familia = Familia.objects.filter(email=email).filter(password=senha)

    if len(familia) == 0:
          return redirect('/login/familia/?status=1')

    elif len(familia) > 0:
        # request.session['status'] = {True, familia[0].id, familia[0].nome }

        request.session['logado'] = True
        request.session['familia'] = familia[0].nome
        request.session['familia_id'] = familia[0].id
        context = {
                'logado' : request.session['logado'],
                'familia': request.session['familia'],
                'familia_id': request.session['familia_id']
        }
        return render(request, 'portal/home.html', context)


def sair_familia(request):
    request.session.flush()
    return redirect('/login/familia/?status=3')

# FAMILIA

def lista_familia(request):
    if request.session['logado']:
         if request.session.get('familia') != 'Administrador':
            sua_familia = Familia.objects.filter(nome__exact=(request.session['familia']))
            context = {
                 'familia':sua_familia,
                 'logado': request.session['logado'],
                 'familia_id':request.session['familia_id']

            }
         else:
             listfamilia = Familia.objects.all()

             context = {
               'familia': listfamilia,
               'logado': request.session['logado'],
               'familia_id': request.session['familia_id']
             }
         return render(request, 'portal/familia.html',context)
    else:
         return redirect('/login/familia/?status=2')


def familia_add(request):
    form = FamiliaForm(request.POST or None)

    if request.POST:
        if form.is_valid():

            form.save()
            return redirect('familia')

    context = {
        'form': form,

    }
    return render(request, 'portal/familia_add.html', context)


def familia_edit(request, familia_pk):
    family = Familia.objects.get(pk=familia_pk)
    form = FamiliaForm(request.POST or None, instance=family)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('familia')

    context = {
        'form': form,
    }
    return render(request, 'portal/familia_edit.html', context)


def familia_delete(request, familia_pk):
    familia = Familia.objects.get(pk=familia_pk)
    familia.delete()
    return redirect('familia')

# RESPONSÁVEL

def lista_responsavel(request):
    if request.session['logado']:
        if request.session.get('familia') != 'Administrador':
            listfamilia = Responsavel.objects.filter(familia__exact=(request.session['familia_id']))
            context = {
                'responsavel': listfamilia,
                'logado': request.session['logado'],
                'familia_id':request.session['familia_id'],

            }
        else:
            listfamilia = Responsavel.objects.all()

            context = {
                'responsavel': listfamilia,
                'logado': request.session['logado'],
                'familia_id': request.session['familia_id'],
            }
        return render(request, 'portal/responsavel.html', context)
    else:
        return redirect('/login/familia/?status=2')


def responsavel_add(request):
    form = ResponsavelForm(request.POST)

    if request.session.get('logado'):

        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('responsaveis')

        context = {
            'form': form,
            'familia_id': request.session['familia_id'],

        }
        return render(request, 'portal/responsavel_add.html', context)
    else:
        return redirect('/login/familia/?status=2')


def responsavel_edit(request, responsavel_pk):
    responsavel = Responsavel.objects.get(pk=responsavel_pk)
    form = FamiliaForm(request.POST or None, instance=responsavel)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('responsaveis')

    context = {
        'form': form,
    }
    return render(request, 'portal/responsavel_edit.html', context)


def responsavel_delete(request, responsavel_pk):
    responsavel = Familia.objects.get(pk=responsavel_pk)
    responsavel.delete()
    return redirect('responsaveis')


# DEPENDENTE

def lista_dependente(request):
    if request.session['logado']:
        if (request.session['familia']) != 'Administrador':
            seus_dependentes = Dependente.objects.filter(familia__exact=(request.session['id_familia']))

            context = {
                'familia': seus_dependentes,
                'logado': request.session['logado'],
            }
        else:
            listdependente = Dependente.objects.all()

            context = {
                'familia': listdependente,
                'logado': request.session['logado'],
            }
        return render(request, 'portal/dependente.html', context)
    else:
        return redirect('/login/familia/?status=2')



def dependente_add(request):
    form = DependenteForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('dependentes')

    context = {
        'form': form,

    }
    return render(request, 'portal/dependente_add.html' , context)


def dependente_edit(request, dependente_pk):
    dependente = Dependente.objects.get(pk=dependente_pk)
    form = DependenteForm(request.POST or None, instance=dependente)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('dependentes')

    context = {
        'form': form,
    }
    return render(request, 'portal/dependente.html', context)


def dependente_delete(request, dependente_pk):
    dependente = Dependente.objects.get(pk=dependente_pk)
    dependente.delete()
    return redirect('dependentes')


def lista_cuidador(request):
    if request.session['logado']:
        if (request.session['familia']) != 'Administrador':
            seus_cuidadores = Cuidador.objects.filter(familia__exact=(request.session['id_familia']))

            context = {
                'familia': seus_cuidadores,
                'logado': request.session['logado'],
            }
        else:
            listcuidador = Cuidador.objects.all()

            context = {
                'familia': listcuidador,
                'logado': request.session['logado'],
            }
        return render(request, 'portal/cuidador.html', context)
    else:
        return redirect('/login/familia/?status=2')


def cuidador_add(request):
    form = CuidadorForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cuidadores')

    context = {
        'form': form,

    }
    return render(request, 'portal/cuidador_add.html', context)









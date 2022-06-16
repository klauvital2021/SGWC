from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from portal.forms import ResponsavelForm, CuidadorForm, DependenteForm, FamiliaForm
from portal.models import Responsavel, Cuidador, Dependente, Familia

class HomePageView(TemplateView):
    template_name = "portal/home.html"

#def home(request):
#    return render(request, 'portal/home.html')
'''
def login(request):
    if request.method == "GET":
        email = request.GET('email')
        senha = request.GET('senha')

        busca = Q(
            Q(email=email)
            & Q(senha=senha)
        )
        Listfamilia = Familia.objects.filter(busca)
        if Listfamilia.count() != 0:
                acesso = True
                nomeFamilia = Familia.nome
                frase = "Bem vindo ao sistema SGWC"

                context = {
                    'familia': nomeFamilia,
                    'frase': frase,
                }
                return render(request, 'portal/responsavel.html', context=context)

        else:
                frase = "Não existe 'FAMÍLIA' cadastrada com os dados acima"
                acesso = False

                context = {
                'frase': frase,
                'acesso': acesso,
                 }

                return render(request, 'portal/home.html', context=context)
'''
def lista_responsavel(request):
    responsaveis = Responsavel.objects.all()

    context = {
        'responsaveis': responsaveis
    }
    return render(request, 'portal/responsavel.html', context)

def lista_dependente(request):
    dependentes = Dependente.objects.all()
    context = {
        'dependentes': dependentes
    }
    return render(request, 'portal/dependente.html', context)

def lista_cuidador(request):
    cuidadores = Responsavel.objects.all()
    context = {
        'cuidadores': cuidadores
    }
    return render(request, 'portal/cuidador.html', context)

def lista_familia(request):
    familia = Familia.objects.all()
    context = {
        'familia': familia
    }
    return render(request, 'portal/familia.html', context)


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


def responsavel_add(request):
    form = ResponsavelForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('responsaveis')

    context = {
        'form': form,
    }
    return render(request, 'portal/responsavel_add.html', context)

def dependente_add(request):
    form = DependenteForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('dependentes')

    context = {
        'form': form,
    }
    return render(request, 'portal/dependente_add.html', context)

def cuidador_add(request):
    form = DependenteForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cuidadores')

    context = {
        'form': form,
    }
    return render(request, 'portal/cuidador_add.html', context)


'''
def imovel_edit(request, imovel_pk):
    imovel = get_object_or_404(Imovel, pk=imovel_pk)
    form = ImovelForm(instance=imovel)

    if (request.method == 'POST'):
        form = ImovelForm(request.POST, instance=imovel)

        if (form.is_valid()):
            imovel = form.save(commit=False)
            imovel.save()
            return redirect('imoveis')
        else:
            return render(request, 'portal/imovel_edit.html', {'form': form, 'post': imovel})

    elif (request.method == 'GET'):
        return render(request, 'portal/imovel_edit.html', {'form': form, 'post': imovel})

def ross(request):
    ross = Tabelarossheideck.objects.all()
    context = {
        'ross': ross
    }
    return render(request, 'portal/tabela_ross.html', context=context)

def vida_util(request):
    util = Vidautil.objects.all()
    context = {
        'lista': util
    }
    return render(request, 'portal/vida_util.html', context)

def imovel_delete(request, imovel_pk):
    imovel = Imovel.objects.get(pk=imovel_pk)
    imovel.delete()
    return redirect('imoveis')


def padrao (request):
    padrao = Padrao.objects.all()
    context = {
        'padrao': padrao
    }
    return render(request, 'portal/padrao.html', context)

def padrao_add(request):
    form = PadraoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('padrao')

    context = {
        'form': form,
    }
    return render(request, 'portal/padrao_add.html', context)

def condominio (request):
    condominio = Nomecondominio.objects.all()
    context = {
        'condominio': condominio
    }
    return render(request, 'portal/condominio.html', context)

def cond_add(request):
    form = NomecondominioForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('condominio')

    context = {
        'form': form,
    }
    return render(request, 'portal/cond_add.html', context)


def cond_edit(request, cond_pk):
    condominio = Nomecondominio.objects.get(pk=cond_pk)

    form = NomecondominioForm(request.POST or None, instance=condominio)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('condominio')

    context = {
        'form': form,
    }
    return render(request, 'portal/cond_edit.html', context)

def cond_delete(request, cond_pk):
    condominio = Imovel.objects.get(pk=cond_pk)
    condominio.delete()

    return redirect('condominio')

def estadoConserv (request):
    estadoConservacao = Estadoconser.objects.all()
    context = {
        'estadoCons': estadoConservacao
    }
    return render(request, 'portal/estadoConservacao.html', context)

def estadoConserv_add(request):
    form = EstadoconserForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('estadoConservacao')

    context = {
        'form': form,
    }
    return render(request, 'portal/estadoConservacao_add.html', context)


def tipo(request):
    tipos = Tipo.objects.all()
    context = {
        'tipos': tipos
    }
    return render(request, 'portal/tipo.html', context)


def tipo_add(request):
    form = TipoForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('tipo')

    context = {
        'form': form,
    }

    return render(request, 'portal/tipo_add.html', context)
    '''
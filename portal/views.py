from django.views.generic import TemplateView, CreateView
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.db.models import Q
from hashlib import sha256
from django.contrib.auth.decorators import login_required
from portal.forms import ResponsavelForm, CuidadorForm, DependenteForm, FamiliaForm, ConsultaForm, MedicamentoForm, PosConsultaForm
from portal.models import Responsavel, Cuidador, Dependente, Familia, Consultas, Pos_Consultas, Medicamentos
from django.contrib.sessions.middleware import SessionMiddleware


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

    familia = Familia.objects.filter(email=email).filter(senha=senha)

    if len(familia) == 0:
          return redirect('/login/familia/?status=1')

    elif len(familia) > 0:
         #request.session['status'] = { True, familia[0].id, familia[0].nome }

        request.session['logado'] = True
        request.session['familia'] = familia[0].nome
        request.session['familia_id'] = familia[0].id
        context = {
                'logado' : request.session.get('logado'),
                'familia': request.session.get('familia'),
                'familia_id': request.session.get('familia_id')
        }
        return render(request, 'portal/home.html', context)


def sair_familia(request):
    request.session.flush()
    return redirect('/login/familia/?status=3')

# FAMILIA

def lista_familia(request):
   if request.session.get('logado'):
         if request.session.get('familia') != 'Administrador':
             sua_familia = Familia.objects.filter(nome__exact=(request.session['familia']))
             context = {
                     'familia':sua_familia,
                     'logado': request.session.get('logado'),
                     'familia_id':request.session.get('familia_id'),
             }
         else:
             listfamilia = Familia.objects.all()

             context = {
               'familia': listfamilia,
               'logado': request.session.get('logado'),
               'familia_id': request.session.get('familia_id')

                }
         return render(request, 'portal/familia.html', context)
   else:
         return redirect('/login/familia/?status=2')


def familia_add(request):

    form = FamiliaForm(request.POST or None)
    if request.POST:
        if form.is_valid():
           form.save()
           return redirect('/portal/familia/?status=1')

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
    if request.session.get('logado'):
        if request.session.get('familia') != 'Administrador':
            listfamilia = Responsavel.objects.filter(familia__exact=(request.session.get('familia_id')))
            context = {
                'responsavel': listfamilia,
                'logado': request.session.get('logado'),
                'familia_id':request.session.get('familia_id'),

            }
        else:
            listfamilia = Responsavel.objects.all()

            context = {
                'responsavel': listfamilia,
                'logado': request.session.get('logado'),
                'familia_id': request.session.get('familia_id'),
            }
        return render(request, 'portal/responsavel.html', context)
    else:
        return redirect('/login/familia/?status=2')


def responsavel_add(request):
    familia_id = request.session.get('familia_id')
    if request.method == "GET":
        form = ResponsavelForm()
        context = {
            'form': form,
            'familia': Responsavel.familia
        }
        return render(request, 'portal/responsavel_add.html', context)
    else:
        form = ResponsavelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('responsaveis')

        context = {
            'form': form,
            'familia': familia_id
        }
    return render(request, 'portal/responsavel_add.html', context)


def responsavel_edit(request, responsavel_pk):
    responsavel = Responsavel.objects.get(pk=responsavel_pk)
    form = ResponsavelForm(request.POST or None, instance=responsavel)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('responsaveis')

    context = {
        'form': form,
    }
    return render(request, 'portal/responsavel_edit.html', context)


def responsavel_delete(request, responsavel_pk):
    responsavel = Responsavel.objects.get(pk=responsavel_pk)
    responsavel.delete()
    return redirect('responsaveis')


# DEPENDENTE

def lista_dependente(request):
    if request.session.get('logado'):
        if request.session.get('familia') != 'Administrador':
            listfamilia = Dependente.objects.filter(familia__exact=(request.session.get('familia_id')))
            context = {
                'dependentes': listfamilia,
                'logado': request.session.get('logado'),
                'familia_id': request.session.get('familia_id'),

            }
        else:
            listfamilia = Dependente.objects.all()

            context = {
                'dependentes': listfamilia,
                'logado': request.session.get('logado'),
                'familia_id': request.session.get('familia_id'),
            }
        return render(request, 'portal/dependente.html', context)
    else:
        return redirect('/login/familia/?status=2')


def dependente_add(request):
    familia_id = request.session.get('familia_id')
    form = DependenteForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('dependentes')

    context = {
        'form': form,
        'familia': familia_id
    }
    return render(request, 'portal/dependente_add.html', context)


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
    return render(request, 'portal/dependente_edit.html', context)


def dependente_delete(request, dependente_pk):
    dependente = Dependente.objects.get(pk=dependente_pk)
    dependente.delete()
    return redirect('dependentes')


def lista_cuidador(request):
    if request.session.get('logado'):
        if request.session.get('familia') != 'Administrador':
            listfamilia = Cuidador.objects.filter(familia__exact=(request.session.get('familia_id')))
            context = {
                'cuidadores': listfamilia,
                'logado': request.session.get('logado'),
                'familia_id': request.session.get('familia_id'),

            }
        else:
            listfamilia = Cuidador.objects.all()

            context = {
                'cuidadores': listfamilia,
                'logado': request.session.get('logado'),
                'familia_id': request.session.get('familia_id'),
            }
        return render(request, 'portal/cuidador.html', context)
    else:
        return redirect('/login/familia/?status=2')


def cuidador_add(request):
    familia_id = request.session.get('familia_id')
    form = CuidadorForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cuidadores')

    context = {
        'form': form,
        'familia': familia_id
    }
    return render(request, 'portal/cuidador_add.html', context)

def cuidador_edit(request, cuidador_pk):
    cuidador = Cuidador.objects.get(pk=cuidador_pk)
    form = CuidadorForm(request.POST or None, instance=cuidador)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('cuidadores')

    context = {
        'form': form,
    }
    return render(request, 'portal/cuidador_edit.html', context)


def cuidador_delete(request, cuidador_pk):
    cuidador = Cuidador.objects.get(pk=cuidador_pk)
    cuidador.delete()
    return redirect('cuidadores')

# Consultas
def lista_consulta(request):
    if request.session.get('logado'):
        if request.session.get('familia') != 'Administrador':
            listConsulta = Consultas.objects.filter(dependente__familia =(request.session.get('familia_id')))
            context = {
                'familia':  listConsulta,
                'logado': request.session.get('logado'),
                'familia_id':request.session.get('familia_id'),

            }
        else:
            listConsulta = Consultas.objects.all()

            context = {
                'consultas': listConsulta,
                'logado': request.session.get('logado'),
                'familia_id': request.session.get('familia_id'),
            }
        return render(request, 'portal/consultas.html', context)
    else:
        return redirect('/login/familia/?status=2')


def consulta_add(request):
    dependentes = Dependente.objects.filter(familia=request.session.get('familia_id'))

    if request.method == "GET":
        ConsultaForm.dependente = dependentes
        form = ConsultaForm()

        context = {
            'form': form,

        }

    else:
        ConsultaForm.dependente = dependentes
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('consultas')

        context = {
            'form': form,

        }
    return render(request, 'portal/consulta_add.html', context)


def consulta_edit(request, consulta_pk):
    consulta = Consultas.objects.get(pk=consulta_pk)
    form = ConsultaForm(request.POST or None, instance=consulta)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('consulta')

    context = {
        'form': form,
    }
    return render(request, 'portal/consulta_edit.html', context)


def consulta_delete(request, consulta_pk):
    consulta = Consultas.objects.get(pk=consulta_pk)
    consulta.delete()
    return redirect('consultas')


# Pós Consultas
def lista_posconsulta(request):
    if request.session.get('logado'):
        if request.session.get('familia') != 'Administrador':
            listPosConsulta = Pos_Consultas.objects.filter(consulta__dependente__familia=(request.session.get('familia_id')).filter(consulta__pos_consultas=Consultas.id))

            context = {
                'posconsulta':  listPosConsulta,
                'logado': request.session.get('logado'),
                'familia_id':request.session.get('familia_id'),

            }
        else:
            listPosConsulta  = Pos_Consultas.objects.all()

            context = {
                'posconsulta':  listPosConsulta,
                'logado': request.session.get('logado'),
                'familia_id': request.session.get('familia_id'),
            }
        return render(request, 'portal/posconsulta.html', context)
    else:
        return redirect('/login/familia/?status=2')


def posconsulta_add(request):
    familia_id = request.session.get('familia_id')
    if request.method == "GET":
        form = PosConsultaForm()
        context = {
            'form': form,
            'familia': familia_id
        }

    else:
        form = PosConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posconsulta')

        context = {
            'form': form,
            'familia': familia_id
        }
    return render(request, 'portal/posconsulta_add.html', context)


def posconsulta_edit(request, posconsulta_pk):
    posconsulta = Pos_Consultas.objects.get(pk=posconsulta_pk)
    form = PosConsultaForm(request.POST or None, instance=posconsulta)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('posconsulta')

    context = {
        'form': form,
    }
    return render(request, 'portal/posconsulta_edit.html', context)


def posconsulta_delete(request, consulta_pk):
    posconsulta = Pos_Consultas.objects.get(pk=consulta_pk)
    posconsulta.delete()
    return redirect('posconsulta')


# Medicamentos
def lista_medicamento(request):
    if request.session.get('logado'):
        if request.session.get('familia') != 'Administrador':
            listMedicamento = Medicamentos.objects.filter(dependente__familia=(request.session.get('familia_id')))

            context = {
                'medicamentos':  listMedicamento,
                'logado': request.session.get('logado'),
                'familia_id':request.session.get('familia_id'),

            }
        else:
            listMedicamento  = Medicamentos.objects.all()

            context = {
                'medicamentos':  listMedicamento,
                'logado': request.session.get('logado'),
                'familia_id': request.session.get('familia_id'),
            }
        return render(request, 'portal/medicamentos.html', context)
    else:
        return redirect('/login/familia/?status=2')


def medicamentos_add(request):
    familia_id = request.session.get('familia_id')
    if request.method == "GET":
        form = MedicamentoForm()
        context = {
            'form': form,
            'familia': familia_id
        }

    else:
        form = MedicamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medicamento')

        context = {
            'form': form,
            'familia': familia_id
        }
    return render(request, 'portal/medicamentos_add.html', context)


def medicamento_edit(request, medicamento_pk):
    medicamento = Medicamentos.objects.get(pk=medicamento_pk)
    form = MedicamentoForm(request.POST or None, instance=medicamento)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('medicamento_edit')

    context = {
        'form': form,
    }
    return render(request, 'portal/medicamentos_edit.html', context)


def medicamento_delete(request, medicamento_pk):
    medicamento = Pos_Consultas.objects.get(pk=medicamento_pk)
    medicamento.delete()
    return redirect('medicamento')



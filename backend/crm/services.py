from django.contrib.auth.models import Group, User

from backend.core.services import add_permissions


def user_create(form):
    first_name = form.cleaned_data.get('first_name')
    last_name = form.cleaned_data.get('last_name')
    email = form.cleaned_data.get('email')
    user = User.objects.create(
        username=email,
        first_name=first_name,
        last_name=last_name,
        email=email,
    )
    return user


def add_to_group_responsavel(form, user):
    # Adiciona o Responsavel no grupo 'responsavel'.
    group = Group.objects.get(name='responsavel')
    user.groups.add(group)

    # Adiciona a permissão can_view_familia.
    add_permissions('responsavel', ['view_familia'])


def add_to_group_cuidador(form, user):
    # Adiciona o Responsavel no grupo 'cuidador'.
    group = Group.objects.get(name='cuidador')
    user.groups.add(group)

    # Adiciona a permissão can_view_familia.
    add_permissions('cuidador', ['view_cuidador'])
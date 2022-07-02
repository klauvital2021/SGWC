from django.contrib.auth.models import Group, Permission


def add_permissions(group_name, permissions):
    group = Group.objects.get(name=group_name)
    permissions = Permission.objects.filter(codename__in=permissions)
    # Remove todas as permissões.
    group.permissions.clear()
    # Adiciona novas permissões.
    for perm in permissions:
        group.permissions.add(perm)

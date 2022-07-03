from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from backend.crm.models import Usuario


@login_required
def home(request):
    user = request.user
    usuario = Usuario.objects.filter(user=user).first()
    context = {'familia': usuario.familia}
    return render(request, 'home.html', context)

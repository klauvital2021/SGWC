from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import ResponsavelPrincipalForm
from .services import responsavel_create


def responsavel_principal_add(request):
    template_name = 'accounts/responsavel_principal_add.html'
    form = ResponsavelPrincipalForm(request.POST or None)
    success_url = reverse_lazy('home')

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            responsavel_create(form, user)
            return redirect(success_url)

    context = {'form': form}
    return render(request, template_name, context)

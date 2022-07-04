from .models import Usuario

def retorno_familia(request):
   user = request.user
   usuario = Usuario.objects.filter(user=user).first()
   familia = usuario.familia
   context = {'familia': familia}
   return context
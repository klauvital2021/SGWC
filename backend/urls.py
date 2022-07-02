from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backend.core.urls')),
    path('accounts/', include('backend.accounts.urls')),
    path('crm/', include('backend.crm.urls')),
    path('consulta/', include('backend.consulta.urls')),
]

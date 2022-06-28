from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portal.urls')),
    path('portal/', include('portal.urls')),
    path('accounts/', include('allauth.urls')),
    path('portal/', include('django.contrib.auth.urls')),

]

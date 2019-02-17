from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('appCode.urls')),
    path('admin/', admin.site.urls),
    path('', include('usuario.urls')),
]

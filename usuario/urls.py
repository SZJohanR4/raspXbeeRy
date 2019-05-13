from django.urls import path, include
from django.conf import settings
from . import views
from usuario.api import *

app_name = 'usuario'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('usuario/', views.userPerfil, name='userPerfil'),
    #path('pedidos', include('producto.urls')),

    path('usuario/prueba/', SearchPeopledataView.as_view(), name='search_people'),
]

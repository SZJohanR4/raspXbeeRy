from django.urls import path, include
from django.conf import settings
from . import views
app_name = 'usuario'

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('usuario/', views.userPerfil, name='userPerfil'),
    #path('pedidos', include('producto.urls')),
]

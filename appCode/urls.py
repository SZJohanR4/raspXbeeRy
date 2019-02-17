from django.conf import settings
from django.urls import path, include
from . import views

app_name = 'appCode'

urlpatterns = [
    path('', views.index, name='index'),
    path('conexiones/', views.conexiones, name='conexiones'),
    path('red/', views.red, name='red'),
    path('cloud_conector/', views.cloud_conector, name='cloud_conector'),
    path('herramientas/', views.herramientas, name='herramientas'),
    path('sistema/', views.sistema, name='sistema'),
    path('consola/', views.consola, name='consola'),
    path('consola/comando', views.comando, name='comando'),
]

from django.conf import settings
from django.urls import path, include
from . import views

app_name = 'appCode'

urlpatterns = [
    path('', views.index, name='index'),

    #conexiones paths
    path('conexiones/', views.conexiones, name='conexiones'),
    path('conexiones/ethernet', views.conexiones, name='conexiones_ethernet'),
    path('conexiones/wifi', views.conexionesWifi, name='conexiones_wifi'),
    path('conexiones/clients', views.conexionesClients, name='conexiones_clients'),
    path('conexiones/gprs', views.conexionesGPRS, name='conexiones_gprs'),

    #red paths
    path('red/', views.red, name='red'),
    path('red/sensor_inf', views.red, name='sensor_inf'),
    path('red/sensor_log', views.sensorLog, name='sensorLog'),
    path('red/sensor_map/', views.sensorMap, name='sensorMap'),
    path('red/nodos_conectados', views.nodosConectados, name='nodosConectados'),

    #cloud conector paths
    path('cloud_conector/', views.cloudConector, name='cloudConector'),

    #herrmaientas paths
    path('herramientas/', views.herramientas, name='herramientas'),
    path('herramientas/ping', views.herramientas, name='herramientas'),
    path('herramientas/tracer', views.tracer, name='tracer'),

    #sistema paths
    path('sistema/', views.sistema, name='sistema'),

    #data paths
    path('data/', views.data, name='data'),
    path('data/get_data', views.data, name='get_data'),
    path('data/admin_tablas', views.adminTablas, name='adminTablas'),
    path('data/sync', views.sync, name='sync'),


    path('consola/', views.consola, name='consola'),
    path('consola/comando', views.comando, name='comando'),
]

from django.conf import settings
from django.urls import path, include
from . import views
from appCode.api import *

app_name = 'appCode'

urlpatterns = [
    path('', views.index, name='index'),

    #conexiones paths
    path('conexiones/ethernet', views.conexiones, name='conexiones_ethernet'),
    path('conexiones/wifi', views.conexionesWifi, name='conexiones_wifi'),
    path('conexiones/clients', views.conexionesClients, name='conexiones_clients'),
    path('conexiones/gprs', views.conexionesGPRS, name='conexiones_gprs'),

    #red paths
    path('red/sensor_inf', views.red, name='sensor_inf'),
    path('red/sensor_log', views.sensorLog, name='sensorLog'),
    path('red/sensor_mp', views.sensorMap, name='sensorMap'),
    path('red/nodos_conectados', views.nodosConectados, name='nodosConectados'),
    path('red/sensor_inf_form/', SensorInfo.as_view(), name='sensor_inf_form'),
    path('red/get_sensor_inf/', SensorInfo.as_view(), name='get_sensor_inf'),

    #cloud conector paths
    path('cloud_conector/', views.cloudConector, name='cloudConector'),

    #herrmaientas paths
    path('herramientas/ping', views.herramientas, name='herramientas'),
    path('herramientas/tracer', views.tracer, name='tracer'),

    #sistema paths
    path('sistema/', views.sistema, name='sistema'),

    #data paths
    path('data/get_data', views.data, name='get_data'),
    path('data/admin_tablas', views.adminTablas, name='adminTablas'),
    path('data/sync', views.sync, name='sync'),


    path('consola/', views.consola, name='consola'),
    path('consola/load_data/', CreateDataset.as_view(), name='load_data'),

    #Data Science
    path('usuario/model_predict/', CreateDataset.as_view(), name='get_model_predict'),
]

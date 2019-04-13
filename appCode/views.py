from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import CloudForm
from .forms import ethernetConexForm
from .forms import gprsConexForm
from .forms import pingToolForm
from .forms import sensorRedForm
from .forms import tracerToolForm
from .forms import wifiConexForm
from .forms import ziggbeeRedForm
from .forms import searchdataForm
from .forms import DateForm
from usuario.forms import loginForm
import serial #pip install pyserial


# Create your views here.
def index(request):
    return render(request,'index.html',{"form":loginForm})

#conexiones views
@login_required(login_url='/')
def conexiones(request):
    return render(request,'Conexiones/conexionEthernet.html',{"form":ethernetConexForm})

@login_required(login_url='/')
def conexionesWifi(request):
    return render(request,'Conexiones/conexionWifiAp.html',{"form":wifiConexForm})

@login_required(login_url='/')
def conexionesClients(request):
    return render(request,'Conexiones/conexionClientsConnected.html')

@login_required(login_url='/')
def conexionesGPRS(request):
    return render(request,'Conexiones/conexionGPRS.html',{"form":gprsConexForm})

#red views
@login_required(login_url='/')
def red(request):
    return render(request,'Red/infGateway.html',{"form":sensorRedForm})

@login_required(login_url='/')
def sensorLog(request):
    return render(request,'Red/logGetway.html',{"form":ziggbeeRedForm})

@login_required(login_url='/')
def sensorMap(request):
    return render(request,'Red/mapaSensores.html')

@login_required(login_url='/')
def nodosConectados(request):
    return render(request,'Red/nodosConectados.html')

#cloud_conector views
@login_required(login_url='/')
def cloudConector(request):
    return render(request,'CloudConnector/cloudConnector.html',{"form":CloudForm})

#herramientas views
@login_required(login_url='/')
def herramientas(request):
    return render(request,'Herramientas/ping.html',{"form":pingToolForm})

@login_required(login_url='/')
def tracer(request):
    return render(request,'Herramientas/tracerRoute.html',{"form":tracerToolForm})

#sistema views
@login_required(login_url='/')
def sistema(request):
    return render(request,'Sistema/onOffSistema.html')

#data views
@login_required(login_url='/')
def data(request):
    return render(request,'Data/consultarDB.html',{"form":searchdataForm})

@login_required(login_url='/')
def adminTablas(request):
    return render(request,'Data/adminTablas.html')

@login_required(login_url='/')
def sync(request):
    return render(request,'Data/sincronizarDB.html',{"form":DateForm})

@login_required(login_url='/')
def consola(request):
    return render(request,'Consola/terminal.html')

@csrf_exempt
def comando(request):
    if request.method == 'POST':
        data=request.POST
        comando=(data['command'])
        ser = serial.Serial(
            port='COM3',\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
                timeout=0)

        ser.write(comando.encode('utf-8'))
        print("comando escrito")
        print("====FIN=====")
        ser.close()
        return HttpResponse("Success!") # Sending an success response
    else:
         return HttpResponse("Request method is not a GET")

from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from .forms import sensorRedForm
from .models import Node

#data Science
import numpy as np
import pandas as pd


class SensorInfo(APIView):
    authentication_classes = (TokenAuthentication, )

    def get(self, request):
        #print ("https://codepen.io/tutelagesystems/pen/YygBGg")
        #print ("https://stackoverflow.com/questions/40069455/basic-vue-js-2-and-vue-resource-http-get-with-variable-assignment")
        data = []
        nodos = Node.objects.all()

        for item in nodos:
            nodo = {
            'id': item.id,
            'ip': item.ip,
            'latitude': item.latitude,
            'longitude': item.longitude,
            'mac': item.mac,
            }
            data.append(nodo)
        response = {'nodos': data}
        return JsonResponse(response, safe=False)

    def post(self, request):
        if request.method == 'POST':
            form = sensorRedForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                ip = form.cleaned_data['ip']
                latitude = form.cleaned_data['latitude']
                longitude = form.cleaned_data['longitude']
                mac = form.cleaned_data['mac']
                node = Node(ip = ip, latitude = latitude, longitude = longitude,
                 mac = mac)
                node.save()
                return HttpResponseRedirect('/red/sensor_inf')
        else:
            form = sensorRedForm()
        return render(request, 'Red/infGateway.html',{"form":sensorRedForm})

class CreateDataset(APIView):
    def get(self, request):

        # Create the pandas DataFrame
        df_node_1 = pd.DataFrame()
        df_node_1['Date'] = pd.date_range('20180101', periods=1000)
        df_node_1['Nodo'] = 1
        df_node_1['Velocidad_Cauce'] = np.random.randint(1,4, size=1000)
        df_node_1['Area_Cauce'] = 4
        df_node_1['Caudal'] = df_node_1['Velocidad_Cauce']*df_node_1['Area_Cauce']
        df_node_1['Lluvia'] = 4


        df_node_2 = pd.DataFrame()
        df_node_2['Date'] = pd.date_range('20180101', periods=1000)
        df_node_2['Nodo'] = 2
        df_node_2['Velocidad_Cauce'] = np.random.randint(1,4, size=1000)
        df_node_2['Area_Cauce'] = 6
        df_node_2['Caudal'] = df_node_2['Velocidad_Cauce']*df_node_2['Area_Cauce']
        df_node_2['Lluvia'] = 4


        df_node_3 = pd.DataFrame()
        df_node_3['Date'] = pd.date_range('20180101', periods=1000)
        df_node_3['Nodo'] = 3
        df_node_3['Velocidad_Cauce'] = np.random.randint(1,4, size=1000)
        df_node_3['Area_Cauce'] = 6
        df_node_3['Caudal'] = df_node_3['Velocidad_Cauce']*df_node_3['Area_Cauce']
        df_node_3['Lluvia'] = 4

        df_node_result = pd.concat([df_node_1, df_node_2, df_node_3])
        print (df_node_result)
        print(df_node_result.describe())
        return HttpResponse("Running data")

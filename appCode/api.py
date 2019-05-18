from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from .forms import sensorRedForm
from .models import Node

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

# Created by L.S. Urrea [lurreaferia@uniminuto.edu.co], J. Sanchez-Rojas [jsanchezro8@uniminuto.edu.co], & C.A.Sierra [carlos.andres.sierra.v@gmail.com] on May 2019.

# Collaboration acknowlegments: María Fernanda Chaparro & Fernando & Santiago Salazar.

# Copyright (c) 2019 L.S. Urrea, J. Sanchez-Rojas, & C.A.Sierra. Research Group on Athenea. All rights reserved.

#

# This file is part of RaspXbee Project.

#

# RaspXbee Project is free software: you can redistribute it and/or modify it under the terms of the

# GNU General Public License as published by the Free Software Foundation, version 3
from datetime import date
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from .forms import sensorRedForm
from .models import Cauce
from .models import Node

#data Science
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston

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

class SensorMap(APIView):
    authentication_classes = (TokenAuthentication, )

    def get(self, request):
        #print ("https://codepen.io/tutelagesystems/pen/YygBGg")
        #print ("https://stackoverflow.com/questions/40069455/basic-vue-js-2-and-vue-resource-http-get-with-variable-assignment")
        data = []
        causes = Cauce.objects.all()
        print("------",causes)
        for item in causes:
            nodo = {
            'velocidad': item.velocidad,
            'area': item.area,
            'cauce': item.cauce,
            'lluvia': item.lluvia,
            'status': item.status,
            }
            data.append(nodo)
        response = {'causes': data}
        return JsonResponse(response, safe=False)

class CreateDataset(APIView):
    def get_data_frame(self):
        # Create the pandas DataFrame
        df_node_1 = pd.DataFrame()
        #df_node_1['Date'] = pd.date_range('20180101', periods=1000)
        df_node_1['Velocidad_Cauce'] = np.random.uniform(1,4,70)
        df_node_1['Nodo'] = 1
        df_node_1['Area_Cauce'] = 4
        df_node_1['Caudal'] = df_node_1['Velocidad_Cauce']*df_node_1['Area_Cauce']
        df_node_1['Lluvia'] = np.random.uniform(0,5,70)


        df_node_2 = pd.DataFrame()
        #df_node_2['Date'] = pd.date_range('20180101', periods=1000)
        df_node_2['Velocidad_Cauce'] = np.random.uniform(1,4,70)
        df_node_2['Nodo'] = 2
        df_node_2['Area_Cauce'] = 6
        df_node_2['Caudal'] = df_node_2['Velocidad_Cauce']*df_node_2['Area_Cauce']
        df_node_2['Lluvia'] = np.random.uniform(0,5,70)


        df_node_3 = pd.DataFrame()
        #df_node_3['Date'] = pd.date_range('20180101', periods=1000)
        df_node_3['Velocidad_Cauce'] = np.random.uniform(1,4,70)
        df_node_3['Nodo'] = 3
        df_node_3['Area_Cauce'] = 6
        df_node_3['Caudal'] = df_node_3['Velocidad_Cauce']*df_node_3['Area_Cauce']
        df_node_3['Lluvia'] = np.random.uniform(0,5, 70)

        df_node_result = pd.concat([df_node_1, df_node_2, df_node_3])
        print(df_node_result)
        #print(df_node_result.describe())
        self.save_data(df_node_result)
        return df_node_result

    def save_data(self, df):
        for row in df.values:
            cauce = Cauce(velocidad = row[0], nodo = Node.objects.get(pk = row[1]),
            area = row[2], cauce = row[3], lluvia = row[4], fecha = date.today(),
            status = 1)
            cauce.save()


    def print_df(self, df):
        plt.scatter(df['Caudal'], df['Area_Cauce'], label = 'data1', color='red')
        plt.scatter(df['Caudal'], df['Lluvia'], label = 'data2', color='blue')
        plt.title('Grafico de dispercion')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.legend()
        plt.show()

    def get(self, request):
        df = self.get_data_frame()
        self.print_df(df)
        boston = load_boston()

        X_ent, X_test, y_ent, y_test = train_test_split(df['Caudal'].values.reshape(-1,1),df['Lluvia'].values.reshape(-1,1))

        rl = LinearRegression()
        fit = rl.fit(X_ent, y_ent)
        print(fit)
        score = rl.score(X_test,y_test)

        caudal_y_pred = rl.predict(X_test)
        plt.scatter(X_test, y_test, color = 'black')
        plt.plot(X_test, caudal_y_pred, color = 'blue')
        plt.xlabel('Eje X')
        plt.ylabel('Eje Y')
        plt.legend()
        plt.show()


        df = df.reset_index()
        df = df.to_json()
        response = {'status': "OK FROM SERVER",
                    'df': df, 'score':score}
        return JsonResponse(response, safe=False)

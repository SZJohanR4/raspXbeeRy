
# Created by L.S. Urrea [lurreaferia@uniminuto.edu.co], J. Sanchez-Rojas [jsanchezro8@uniminuto.edu.co], & C.A.Sierra [carlos.andres.sierra.v@gmail.com] on May 2019.

# Collaboration acknowlegments: María Fernanda Chaparro & Fernando & Santiago Salazar.

# Copyright (c) 2019 L.S. Urrea, J. Sanchez-Rojas, & C.A.Sierra. Research Group on Athenea. All rights reserved.

#

# This file is part of RaspXbee Project.

#

# RaspXbee Project is free software: you can redistribute it and/or modify it under the terms of the

# GNU General Public License as published by the Free Software Foundation, version 3
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, StreamingHttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class SearchPeopledataView(APIView):
    authentication_classes = (TokenAuthentication, )

    def get(self, request):
        print ("https://codepen.io/tutelagesystems/pen/YygBGg")
        print ("https://stackoverflow.com/questions/40069455/basic-vue-js-2-and-vue-resource-http-get-with-variable-assignment")
        return HttpResponse("hola from backend")

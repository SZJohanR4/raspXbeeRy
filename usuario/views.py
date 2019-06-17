# Created by L.S. Urrea [lurreaferia@uniminuto.edu.co], J. Sanchez-Rojas [jsanchezro8@uniminuto.edu.co], & C.A.Sierra [carlos.andres.sierra.v@gmail.com] on May 2019.

# Collaboration acknowlegments: María Fernanda Chaparro & Fernando Alvarez & Santiago Salazar.

# Copyright (c) 2019 L.S. Urrea, J. Sanchez-Rojas, & C.A.Sierra. Research Group on Athenea. All rights reserved.

#

# This file is part of RaspXbee Project.

#

# RaspXbee Project is free software: you can redistribute it and/or modify it under the terms of the

# GNU General Public License as published by the Free Software Foundation, version 3
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import loginForm

# Create your views here.
def loginUser(request):
    login_form=loginForm()
    if request.method=='POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username=request.POST['user_name']
            password=request.POST['password']
            user = authenticate(request=request, username=username, password=password)
            if user is not None and user.is_active:
                request.session.set_expiry(86400)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                fail="Datos Incorrectos"
                return render(request,'index.html',{"form":login_form, "fail":fail})
    return render(request,'index.html',{"form":login_form})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/')
def userPerfil(request):
    return render(request,'Usuario/perfil.html')

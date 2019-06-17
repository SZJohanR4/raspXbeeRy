# Created by L.S. Urrea [lurreaferia@uniminuto.edu.co], J. Sanchez-Rojas [jsanchezro8@uniminuto.edu.co], & C.A.Sierra [carlos.andres.sierra.v@gmail.com] on May 2019.

# Collaboration acknowlegments: María Fernanda Chaparro & Fernando Alvarez & Santiago Salazar.

# Copyright (c) 2019 L.S. Urrea, J. Sanchez-Rojas, & C.A.Sierra. Research Group on Athenea. All rights reserved.

#

# This file is part of RaspXbee Project.

#

# RaspXbee Project is free software: you can redistribute it and/or modify it under the terms of the

# GNU General Public License as published by the Free Software Foundation, version 3
from django import forms

#Conexiones forms
class ethernetConexForm(forms.Form):
    TYPE_CONEX_CHOICES = (('DHCP', 'DHCP'),('TCP', 'TCP'),)
    type_conex=forms.ChoiceField(choices = TYPE_CONEX_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'type_conex'}))
    show_info=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'show_info', 'placeholder':'Mostrar info'}))

class wifiConexForm(forms.Form):
    #wifi ap conexion
    address=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'address', 'placeholder':'Mostrar info'}))
    netmask=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'netmask', 'placeholder':'Mostrar info'}))
    boradcast=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'boradcast', 'placeholder':'Mostrar info'}))
    end_alert_to_address=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'end_alert_to_address', 'placeholder':'Mostrar info'}))
    broadcast=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'broadcast', 'placeholder':'Mostrar info'}))
    primary_dns=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'primary_dns', 'placeholder':'Mostrar info'}))
    secondary_dns=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'secondary_dns', 'placeholder':'Mostrar info'}))
    #Radio part
    NUMBER_CHOICES = (('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),)
    essid=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'essid', 'placeholder':'Mostrar info'}))
    channel=forms.ChoiceField(choices = NUMBER_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'channel'}))
    protocol=forms.ChoiceField(choices = NUMBER_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'protocol'}))
    #security
    SECURITY_CHOICES = (('WPA', 'WPA'),('NONE', 'NONE'),)
    security_protocolo=forms.ChoiceField(choices = SECURITY_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'security_protocolo'}))

class gprsConexForm(forms.Form):
    OPERATOR_CHOICES = (('Claro', 'Claro'),('Movistar', 'Movistar'),('Exito', 'Exito'),('Virgin', 'VirginExito'),('Avantel', 'Avantel'),('Tigo', 'Tigo'))
    operator=forms.ChoiceField(choices = OPERATOR_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'operator'}))
    card_pin=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'card_pin', 'placeholder':'Mostrar info'}))
    username=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'username', 'placeholder':'Mostrar info'}))
    password=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'password', 'placeholder':'Password'}))

#Red forms
class sensorRedForm(forms.Form):
    ip=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'ip', 'placeholder':'Ip'}))
    latitude=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'id':'latitude', 'placeholder':'Latitud'}))
    longitude=forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control', 'id':'longitude', 'placeholder':'Longitud'}))
    mac=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'mac', 'placeholder':'Mac'}))

class ziggbeeRedForm(forms.Form):
    gateway=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'gateway', 'placeholder':'Mostrar info'}))

#cloud conector forms
class CloudForm(forms.Form):
    DATA_TYPE_CHOICES = (('String', 'String'),('Int', 'Int'))
    name=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'name', 'placeholder':'Mostrar info'}))
    data_type=forms.ChoiceField(choices = DATA_TYPE_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'data_type'}))
    name_server=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'name_server', 'placeholder':'Mostrar info'}))

#herramientas forms
class pingToolForm(forms.Form):
    INTERFACES_CHOICES = (('Ethernet IPv4', 'Ethernet IPv4'),('Wifi', 'Wifi'),('Gprs', 'GPRS'))
    host=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'host', 'placeholder':'Mostrar info'}))
    interface=forms.ChoiceField(choices = INTERFACES_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'interface'}))

class tracerToolForm(forms.Form):
    INTERFACES_CHOICES = (('Ethernet IPv4', 'Ethernet IPv4'),('Wifi', 'Wifi'),('Gprs', 'GPRS'))
    host=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'host', 'placeholder':'Mostrar info'}))
    interface=forms.ChoiceField(choices = INTERFACES_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'interface'}))

#Data sincronize forms
class DateForm(forms.Form):
    Select=forms.ChoiceField( required=True, widget=forms.Select(attrs={'class':'form-control'}))
    Dates=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'Dates', 'placeholder':'Fecha'}))

#Data forms
class searchdataForm(forms.Form):
    data_Base=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'data_Base', 'placeholder':'Base de datos'}))
    Table=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'Table', 'placeholder':'Tablas'}))
    IP=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'IP', 'placeholder':'IP'}))
    Show_Data=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'Show_Data', 'placeholder':'Informacion'}))
    Port=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'Port', 'placeholder':'Puerto'}))
    User=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'User', 'placeholder':'Usuario'}))
    Pass=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'Pass', 'placeholder':'Contraseña'}))

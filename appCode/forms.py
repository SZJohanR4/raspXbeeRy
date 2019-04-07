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
    operator=forms.ChoiceField(choices = OPERATOR_CHOICES, required=True, widget=forms.Select(attrs={'class':'form-control', 'id':'card_pin'}))
    card_pin=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'card_pin', 'placeholder':'Mostrar info'}))
    username=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'username', 'placeholder':'Mostrar info'}))
    password=forms.CharField(max_length=40,widget=forms.PasswordInput(attrs={'class':'form-control', 'id':'password', 'placeholder':'Password'}))

#Red forms
class sensorRedForm(forms.Form):
    ascii=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'ascii', 'placeholder':'Mostrar info'}))
    fields=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'fields', 'placeholder':'Mostrar info'}))
    type=forms.CharField(max_length=40,widget=forms.TextInput(attrs={'class':'form-control', 'id':'type', 'placeholder':'Mostrar info'}))

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

from django.db import models
from django.contrib.auth.models import User
from appCode.models import Simcard, Ethernet, Wifi

############################# User Model #############################
class User_App(models.Model):
    nickname = models.OneToOneField(User, on_delete = models.CASCADE, default = 'None', unique = True)
    pssword = models.CharField(max_length = 50, default = 'None')
    email = models.EmailField(max_length = 50, default = 'None', unique = True)
    phone = models.CharField(max_length = 15, default = 'None')

    def __str__(self):
        return ("Nickname: %s\tPassword: %s\tEmail: %s\tPhone: %s\n" % (self.nickname, self.password, self.email, self.phone))




############################# Log Model #############################
class Action_Log(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')
    

class Log(models.Model):
    action = models.ForeignKey(Action_Log, on_delete = models.CASCADE, default = 0)
    date_log = models.DateTimeField(auto_now = True)
    user_fk = models.ForeignKey(User_App, on_delete = models.CASCADE, default = 0)
    
    def __str__(self):
        return ("Action: %s\tDate: %s\tUsuario: %s\n" % (self.action, self.date_log, self.user_fk))




############################# Conection Model #############################
class Conection(models.Model):
    date_conn = models.DateTimeField(auto_now = True)
    usuario_fk = models.ForeignKey(User_App, on_delete = models.CASCADE, default = 0)
    simcard_fk = models.ForeignKey(Simcard, on_delete = models.CASCADE, default = 0)
    ethernet_fk = models.ForeignKey(Ethernet, on_delete = models.CASCADE, default = 0)
    wifi_fk = models.ForeignKey(Wifi, on_delete = models.CASCADE, default = 0)
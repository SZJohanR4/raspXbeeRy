from django.db import models
from django.db import connection


############################# GatewayModel #############################
class Status_Gateway_Manager(models.Manager):
    def get_status_gateway(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_status, name AS name_status FROM raspXbeeRy_status_gateway;")
        status_set = cursor.fetchall()
        return status_set
    
    def get_status_gateway_by_id(self, id_):
        cursor = connection.cursor()
        cursor.execute("SELECT name AS name_status FROM raspXbeeRy_status_gateway WHERE id = %s;", [id_])
        status = cursor.fetchall()
        return status
    
    def insert_status_gateway(self, name_, description_):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO raspXbeeRy_status_gateway(name, description) VALUES (%s, %s);", [name_, description_])
        status = cursor.fetchall()
        return status
    
class Status_Gateway(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)
    
    

class Status_Gateway_Manager(models.Manager):
    def get_gateways(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_status, name AS name_status FROM raspXbeeRy_status_gateway;")
        status_set = cursor.fetchall()
        return status_set
    

class Gateway(models.Model):
    name = models.CharField(max_length = 25)
    latitude = models.DecimalField(decimal_places = 6, max_digits = 10)
    longitude = models.DecimalField(decimal_places = 6, max_digits = 10)
    state_fk = models.ForeignKey(Status_Gateway, on_delete = models.CASCADE)
    localAddress = models.CharField(max_length = 50)
    foreingAddress = models.CharField(max_length = 50)

    def __str__(self):
        return ("Name: %s\tLatitude: %s\tLongitude: %s\tState: %s\n" % (self.name, self.latitude, self.longitude, self.state))




############################# Node Model #############################
class Status_Node(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)


class Node(models.Model): 
    ip = models.CharField(max_length=20)
    temperature = models.DecimalField(decimal_places = 2, max_digits = 6)
    voltage = models.DecimalField(decimal_places = 3, max_digits = 6)
    state_fk = models.ForeignKey(Status_Node, on_delete = models.CASCADE)
    latitude = models.DecimalField(decimal_places = 6, max_digits = 10)
    longitude = models.DecimalField(decimal_places = 6, max_digits = 10)
    mac = models.CharField(max_length = 25)
    address_16bits = models.CharField(max_length = 30)

    def __str__(self):
        return ("IP: %s\tTemperature: %s\tVoltage: %s\tState: %s\tLatitude: %s\tLongitude: %s\tMAC: %s\n" % (self.ip, self.temperature, self.voltage, self.state, self.latitude, self.longitude, self.mac))




############################# Wifi Model #############################
class Wifi(models.Model):
    direction = models.CharField(max_length = 25)
    networks_mask = models.CharField(max_length = 25)
    broad_cast = models.CharField(max_length = 25)
    dns_1 = models.CharField(max_length = 40)
    dns_2 = models.CharField(max_length = 40)
    protocol = models.CharField(max_length = 50)
    channel = models.CharField(max_length = 20)

    def __str__(self):
        return ("Direction: %s\tNetwork Mask: %s\tBroadCast: %s\tDNS 1: %s\tDNS 2: %s\tProtocol: %s\tChannel: %s\n" % (self.direction, self.networks_mask, self.broad_cast, self.dns_1, self.dns_2, self.protocol, self.channel))




############################# SimCard Model #############################
class Status_Simcard(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)


class Simcard(models.Model):
    name = models.CharField(max_length = 50)
    operator = models.CharField(max_length = 45)
    card_pin = models.CharField(max_length = 20)
    user_sim = models.CharField(max_length = 30)
    password_sim = models.CharField(max_length = 30)
    state_fk = models.ForeignKey(Status_Node, on_delete = models.CASCADE)

    def __str__(self):
        return ("Name: %s\tOperator: %s\tCard PIN: %s\tUser SIM: %s\tPassword SIM: %s\tState: %s\n" % (self.name, self.operator, self.card_pin, self.user_sim, self.password_sim, self.state))




############################# Ethernet Model #############################
class Status_Ethernet(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)


class Ethernet (models.Model):
    mode = models.CharField(max_length = 20)
    state_fk = models.ForeignKey(Status_Ethernet, on_delete = models.CASCADE)

    def __str__(self):
        return ("Mode: %s\tState: %s\n" % (self.mode, self.state))




############################# Relation Models - M2M Partitions #############################
class Gate_Node(models.Model):
    gateWay_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE)
    nodo_fk = models.ForeignKey(Node, on_delete = models.CASCADE)
    connection = models.DateTimeField(auto_now = True)
    

class Wifi_Gate(models.Model):
    wifi_fk = models.ForeignKey(Wifi, on_delete = models.CASCADE)
    gateway_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE)
    connection = models.DateTimeField(auto_now = True)
    

class Sim_Gate(models.Model):
    simcard_fk = models.ForeignKey(Simcard, on_delete = models.CASCADE)
    gateway_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE)
    connection = models.DateTimeField(auto_now = True)


class Ethernet_Gate(models.Model):
    ethernet_fk = models.ForeignKey(Ethernet, on_delete = models.CASCADE)
    gateWay_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE)
    connection = models.DateTimeField(auto_now = True)  
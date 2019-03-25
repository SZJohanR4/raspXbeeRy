from django.db import models
from django.db import connection



############################# GatewayModel #############################
class States_Gateway_Manager(models.Manager):
    def get_states_gateway(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_states, name AS name_states FROM raspxbeery_states_gateway;")
        states_set = cursor.fetchall()
        return states_set
    
    def insert_states_gateway(self, name_, description_):
        state = States_Gateway(name = name_, description = description_)
        return state

    
class States_Gateway(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)
    states_manager = States_Gateway_Manager()
    
    

class Gateway_Manager(models.Manager):
    def get_gateways(self):
        cursor = connection.cursor()
        cursor.execute("SELECT raspxbeery_gateway.id AS id_gateway, raspxbeery_gateway.name, raspxbeery_gateway.latitude, raspxbeery_gateway.longitude, \
                     raspxbeery_states_gateway.name AS states_name, raspxbeery_gateway.local_address, raspxbeery_gateway.foreing_address \
                     FROM raspxbeery_gateway INNER JOIN raspxbeery_states_gateway ON raspxbeery_states_gateway.id = raspxbeery_gateway.state_fk_id;")
        gateway_set = cursor.fetchall()
        return gateway_set

    def insert_gateways(self, name_, latitude_, longitude_, state_, local_address_, foreing_address_):
        gateway = Gateway(name = name_, latitude = latitude_, longitude = longitude_, state_fk = state_, local_address = local_address_, foreing_address = foreing_address_)
        return gateway
    
    def update_gateway_state(self, id_gateway, new_state):
        cursor = connection.cursor()
        cursor.execute("UPDATE raspxbeery_gateway SET state_fk_id = %s WHERE id = %s;", [new_state, id_gateway])
        gateway = cursor.fetchall()
        return gateway
    
    def update_gateway_location(self, id_gateway, new_latitude, new_longitude):
        cursor = connection.cursor()
        cursor.execute("UPDATE raspxbeery_gateway SET latitude = %s, longitude = %s WHERE id = %s;", [new_latitude, new_longitude, id_gateway])
        gateway = cursor.fetchall()
        return gateway
    
    def update_gateway_local_address(self, id_gateway, new_local):
        cursor = connection.cursor()
        cursor.execute("UPDATE raspxbeery_gateway SET local_address = %s WHERE id = %s;", [new_local, id_gateway])
        gateway = cursor.fetchall()
        return gateway
    
    def update_gateway_foreign_address(self, id_gateway, new_foreign):
        cursor = connection.cursor()
        cursor.execute("UPDATE raspxbeery_gateway SET foreign_address = %s WHERE id = %s;", [new_foreign, id_gateway])
        gateway = cursor.fetchall()
        return gateway
           
    
class Gateway(models.Model):
    name = models.CharField(max_length = 25)
    latitude = models.DecimalField(decimal_places = 6, max_digits = 10)
    longitude = models.DecimalField(decimal_places = 6, max_digits = 10)
    state_fk = models.ForeignKey(States_Gateway, on_delete = models.CASCADE)
    local_address = models.CharField(max_length = 50)
    foreign_address = models.CharField(max_length = 50)
    gateways_manager = Gateway_Manager()

    def __str__(self):
        return ("Name: %s\tLatitude: %s\tLongitude: %s\tState: %s\n" % (self.name, self.latitude, self.longitude, self.state))



class States_Connections_Manager(models.Manager):
    def get_states_gateway(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_states, name AS name_states FROM raspxbeery_states_connection;")
        states_set = cursor.fetchall()
        return states_set
    
    def insert_states_gateway(self, name_, description_):
        state = States_Connection(name = name_, description = description_)
        return state

    
class States_Connection(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)
    states_manager = States_Connections_Manager()




############################# Node Model #############################
class States_Node_Manager(models.Manager):
    def get_states_node(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_states, name AS name_states FROM raspxbeery_states_node;")
        states_set = cursor.fetchall()
        return states_set
    
    def insert_states_node(self, name_, description_):
        state = States_Node(name = name_, description = description_)
        return state


class States_Node(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)
    states_manager = States_Node_Manager()



class Node_Manager(models.Manager):
    def get_nodes(self):
        cursor = connection.cursor()
        cursor.execute("SELECT raspxberry_node.id AS id_node, raspxberry_node.ip, raspxberry_node.temperature, raspxberry_node.voltage, raspxberry_states_node.name,  \
                        raspxberry_node.latitude, raspxberry_node.longitude, raspxberry_node.mac, raspxberry_node.address_16bits \
                        FROM raspxbeery_node INNER JOIN raspxbeery_states_node ON raspxbeery_states_node.id = raspxbeery_node.state_fk_id;")
        node_set = cursor.fetchall()
        return node_set

    def insert_node(self, ip_, temperature_, voltage_, state_, latitude_, longitude_, mac_, address_):
        node = Node(ip = ip_, temperature = temperature_, voltage = voltage_, state_fk = state_, latitude = latitude_, longitude = longitude_, mac = mac_, address = address_)
        return node

    

class Node(models.Model): 
    ip = models.CharField(max_length=20)
    temperature = models.DecimalField(decimal_places = 2, max_digits = 6)
    voltage = models.DecimalField(decimal_places = 3, max_digits = 6)
    state_fk = models.ForeignKey(States_Node, on_delete = models.CASCADE)
    latitude = models.DecimalField(decimal_places = 6, max_digits = 10)
    longitude = models.DecimalField(decimal_places = 6, max_digits = 10)
    mac = models.CharField(max_length = 25)
    address_16bits = models.CharField(max_length = 30)
    node_manager = Node_Manager()

    def __str__(self):
        return ("IP: %s\tTemperature: %s\tVoltage: %s\tState: %s\tLatitude: %s\tLongitude: %s\tMAC: %s\n" % (self.ip, self.temperature, self.voltage, self.state, self.latitude, self.longitude, self.mac))


class Node_Gateway_Manager(models.Manager):
    def get_nodes_gateways(self):
        cursor = connection.cursor()
        cursor.execute("SELECT raspxberry_node.ip AS node_ip, raspxberry_gateway.name AS gateway, raspxberry_node_gateway.connection_date AS connection_date, raspxberry_states_connection.name AS state,  \
                        FROM raspxbeery_node_gate INNER JOIN raspxbeery_node ON raspxbeery_node.id = raspxbeery_node_gate.node_fk_id \
                        INNER JOIN raspxbeery_gateway ON raspxbeery_gateway.id = raspxbeery_node_gate.gateway_fk_id \
                        INNER JOIN raspxbeery_states_connection ON raspxbeery_states_connection.id = raspxbeery_node_gateway.state_fk_id;")
        nodes_set = cursor.fetchall()
        return nodes_set
    
    def get_nodes_by_gateway(self, gateway_):
        cursor = connection.cursor()
        cursor.execute("SELECT raspxberry_node.ip AS node_ip, raspxberry_node_gateway.connection_date AS connection_date, raspxberry_states_connection.name AS state,  \
                        FROM raspxbeery_node_gate INNER JOIN raspxbeery_node ON raspxbeery_node.id = raspxbeery_node_gate.node_fk_id \
                        INNER JOIN raspxbeery_gateway ON raspxbeery_gateway.id = raspxbeery_node_gate.gateway_fk_id \
                        INNER JOIN raspxbeery_states_connection ON raspxbeery_states_connection.id = raspxbeery_node_gateway.state_fk_id \
                        WHERE raspxberry_node_gateway.gateway_fk_id = %s ;", [gateway_])
        nodes_set = cursor.fetchall()
        return nodes_set
    
    def get_nodes_by_gateway_state(self, gateway_, state_):
        cursor = connection.cursor()
        cursor.execute("SELECT raspxberry_node.ip AS node_ip, raspxberry_node_gateway.connection_date AS connection_date, raspxberry_states_connection.name AS state,  \
                        FROM raspxbeery_node_gate INNER JOIN raspxbeery_node ON raspxbeery_node.id = raspxbeery_node_gate.node_fk_id \
                        INNER JOIN raspxbeery_gateway ON raspxbeery_gateway.id = raspxbeery_node_gate.gateway_fk_id \
                        INNER JOIN raspxbeery_states_connection ON raspxbeery_states_connection.id = raspxbeery_node_gateway.state_fk_id \
                        WHERE raspxberry_node_gateway.gateway_fk_id = %s AND raspxberry_node_gateway.state_fk_id = %s;", [gateway_, state_])
        nodes_set = cursor.fetchall()
        return nodes_set
   
    def insert_node_gateway(self, gateway_, node_, state_, connection_):
        node_gateway = Node_Gateway(gateway_fk = gateway_, node_fk = node_, state_fk = state_, connection = connection_)
        return node_gateway


class Node_Gateway(models.Model):
    gateway_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE)
    node_fk = models.ForeignKey(Node, on_delete = models.CASCADE)
    state_fk = models.ForeignKey(States_Connection, on_delete = models.CASCADE)
    connection_date = models.DateTimeField(auto_now = True)




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
class States_Simcard_Manager(models.Manager):
    def get_status_node(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_status, name AS name_status FROM raspxbeery_status_simcard;")
        states_set = cursor.fetchall()
        return states_set
    
    def insert_states_node(self, name_, description_):
        states = States_Simcard(name = name_, description = description_)
        return states


class States_Simcard(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)



class Simcard(models.Model):
    name = models.CharField(max_length = 50)
    operator = models.CharField(max_length = 45)
    card_pin = models.CharField(max_length = 20)
    user_sim = models.CharField(max_length = 30)
    password_sim = models.CharField(max_length = 30)
    state_fk = models.ForeignKey(States_Simcard, on_delete = models.CASCADE)

    def __str__(self):
        return ("Name: %s\tOperator: %s\tCard PIN: %s\tUser SIM: %s\tPassword SIM: %s\tState: %s\n" % (self.name, self.operator, self.card_pin, self.user_sim, self.password_sim, self.state))




############################# Ethernet Model #############################
class States_Ethernet_Manager(models.Manager):
    def get_states_ethernet(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_states, name AS name_states FROM raspxbeery_states_ethernet;")
        status_set = cursor.fetchall()
        return status_set
    
    def insert_states_ethernet(self, name_, description_):
        state = States_Ethernet(name = name_, description = description_)
        return state


class States_Ethernet(models.Model):
    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)


class Ethernet (models.Model):
    mode = models.CharField(max_length = 20)
    state_fk = models.ForeignKey(States_Ethernet, on_delete = models.CASCADE)

    def __str__(self):
        return ("Mode: %s\tState: %s\n" % (self.mode, self.state))




############################# Relation Models - M2M Partitions #############################
    

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
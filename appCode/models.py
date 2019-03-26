from django.db import models
from django.db import connection



############################# GatewayModel #############################
class States_Gateway_Manager(models.Manager):
    def get_states_gateway(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_states, name AS name_states FROM appCode_states_gateway;")
        states_set = cursor.fetchall()
        return states_set
    
    def insert_states_gateway(self, name_, description_):
        state = States_Gateway(name = name_, description = description_)
        return state

    
class States_Gateway(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')
    states_manager = States_Gateway_Manager()
    
    

class Gateway_Manager(models.Manager):
    def get_gateways(self):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_gateway.id AS id_gateway, appCode_gateway.name, appCode_gateway.latitude, appCode_gateway.longitude, \
                     appCode_states_gateway.name AS states_name, appCode_gateway.local_address, appCode_gateway.foreing_address \
                     FROM appCode_gateway INNER JOIN appCode_states_gateway ON appCode_states_gateway.id = appCode_gateway.state_fk_id;")
        gateway_set = cursor.fetchall()
        return gateway_set

    def insert_gateways(self, name_, latitude_, longitude_, state_, local_address_, foreing_address_):
        gateway = Gateway(name = name_, latitude = latitude_, longitude = longitude_, state_fk = state_, local_address = local_address_, foreing_address = foreing_address_)
        return gateway
    
    def update_gateway_state(self, id_gateway, new_state):
        cursor = connection.cursor()
        cursor.execute("UPDATE appCode_gateway SET state_fk_id = %s WHERE id = %s;", [new_state, id_gateway])
        gateway = cursor.fetchall()
        return gateway
    
    def update_gateway_location(self, id_gateway, new_latitude, new_longitude):
        cursor = connection.cursor()
        cursor.execute("UPDATE appCode_gateway SET latitude = %s, longitude = %s WHERE id = %s;", [new_latitude, new_longitude, id_gateway])
        gateway = cursor.fetchall()
        return gateway
    
    def update_gateway_local_address(self, id_gateway, new_local):
        cursor = connection.cursor()
        cursor.execute("UPDATE appCode_gateway SET local_address = %s WHERE id = %s;", [new_local, id_gateway])
        gateway = cursor.fetchall()
        return gateway
    
    def update_gateway_foreign_address(self, id_gateway, new_foreign):
        cursor = connection.cursor()
        cursor.execute("UPDATE appCode_gateway SET foreign_address = %s WHERE id = %s;", [new_foreign, id_gateway])
        gateway = cursor.fetchall()
        return gateway
           
    
class Gateway(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    latitude = models.DecimalField(decimal_places = 6, max_digits = 10, default = 0.0)
    longitude = models.DecimalField(decimal_places = 6, max_digits = 10, default = 0.0)
    state_fk = models.ForeignKey(States_Gateway, on_delete = models.CASCADE, default = 0)
    local_address = models.CharField(max_length = 50, default = 'None')
    foreign_address = models.CharField(max_length = 50, default = 'None')
    gateways_manager = Gateway_Manager()

    def __str__(self):
        return ("Name: %s\tLatitude: %s\tLongitude: %s\tState: %s\n" % (self.name, self.latitude, self.longitude, self.state))



class States_Connections_Manager(models.Manager):
    def get_states_gateway(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_states, name AS name_states FROM appCode_states_connection;")
        states_set = cursor.fetchall()
        return states_set
    
    def insert_states_gateway(self, name_, description_):
        state = States_Connection(name = name_, description = description_)
        return state

    
class States_Connection(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')
    states_manager = States_Connections_Manager()




############################# Node Model #############################
class States_Node_Manager(models.Manager):
    def get_states_node(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_states, name AS name_states FROM appCode_states_node;")
        states_set = cursor.fetchall()
        return states_set
    
    def insert_states_node(self, name_, description_):
        state = States_Node(name = name_, description = description_)
        return state


class States_Node(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')
    states_manager = States_Node_Manager()



class Node_Manager(models.Manager):
    def get_nodes(self):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_node.id AS id_node, appCode_node.ip, appCode_node.temperature, appCode_node.voltage, appCode_states_node.name,  \
                        appCode_node.latitude, appCode_node.longitude, appCode_node.mac, appCode_node.address_16bits \
                        FROM appCode_node INNER JOIN appCode_states_node ON appCode_states_node.id = appCode_node.state_fk_id;")
        node_set = cursor.fetchall()
        return node_set

    def insert_node(self, ip_, temperature_, voltage_, state_, latitude_, longitude_, mac_, address_):
        node = Node(ip = ip_, temperature = temperature_, voltage = voltage_, state_fk = state_, latitude = latitude_, longitude = longitude_, mac = mac_, address = address_)
        return node
    

class Node(models.Model): 
    ip = models.CharField(max_length=20, default = 'None', unique = True)
    state_fk = models.ForeignKey(States_Node, on_delete = models.CASCADE, default = 0)
    latitude = models.DecimalField(decimal_places = 6, max_digits = 10, default = 0.0)
    longitude = models.DecimalField(decimal_places = 6, max_digits = 10, default = 0.0)
    mac = models.CharField(max_length = 25, default = 'None', unique = True)
    address_16bits = models.CharField(max_length = 30, default = 'None', unique = True)
    node_manager = Node_Manager()

    def __str__(self):
        return ("IP: %s\tTemperature: %s\tVoltage: %s\tState: %s\tLatitude: %s\tLongitude: %s\tMAC: %s\n" % (self.ip, self.temperature, self.voltage, self.state, self.latitude, self.longitude, self.mac))



class Node_Register_Manager(models.Manager):
    def get_node_registers(self):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_node.ip, appCode_node_register.temperature, appCode_node_register.voltage, appCode_node_register.register_date \
                        FROM appCode_node_register INNER JOIN appCode_node ON appCode_node.id = appCode_node_register.node_fk_id;")
        node_set = cursor.fetchall()
        return node_set
    
    def get_registers_by_node(self, node_):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_node.ip, appCode_node_register.temperature, appCode_node_register.voltage, appCode_node_register.register_date \
                        FROM appCode_node_register INNER JOIN appCode_node ON appCode_node.id = appCode_node_register.node_fk_id  \
                        WHERE appCpde_node.id = %s;", [node_])
        node_set = cursor.fetchall()
        return node_set
    
    def get_node_registers_by_date(self, date_):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_node.ip, appCode_node_register.temperature, appCode_node_register.voltage, appCode_node_register.register_date \
                        FROM appCode_node_register INNER JOIN appCode_node ON appCode_node.id = appCode_node_register.node_fk_id \
                        WHERE appCode_node_register > %s;", [date_])
        node_set = cursor.fetchall()
        return node_set
    
    def get_node_registers_by_range_date(self, start_date, end_date):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_node.ip, appCode_node_register.temperature, appCode_node_register.voltage, appCode_node_register.register_date \
                        FROM appCode_node_register INNER JOIN appCode_node ON appCode_node.id = appCode_node_register.node_fk_id \
                        WHERE appCode_node_register > %s AND appCode_node_register < %s;", [start_date, end_date])
        node_set = cursor.fetchall()
        return node_set
    
    def insert_node_registers(self, node_ip, temperature_, voltage_):
        node_register = Node_Register(node_fk = node_ip, temperature = temperature_, voltage = voltage_)
        return node_register
    

class Node_Register(models.Model):
    temperature = models.DecimalField(decimal_places = 2, max_digits = 6, default = 0.0)
    voltage = models.DecimalField(decimal_places = 3, max_digits = 6, default = 0.0)
    node_fk = models.ForeignKey(Node, on_delete = models.CASCADE, default = 0)
    register_date = models.DateTimeField(auto_now = True)
    node_register_manager = Node_Register_Manager()

    def __str__(self):
        return ("Node: %s\tDate: %s\tVoltage: %s\tTemperature: %s\n" % (self.node_fk, self.register_date, self.voltage, self.temperature))

    

class Node_Gateway_Manager(models.Manager):
    def get_nodes_gateways(self):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_node.ip AS node_ip, appCode_gateway.name AS gateway, appCode_node_gateway.connection_date AS connection_date, appCode_states_connection.name AS state,  \
                        FROM appCode_node_gate INNER JOIN appCode_node ON appCode_node.id = appCode_node_gate.node_fk_id \
                        INNER JOIN appCode_gateway ON appCode_gateway.id = appCode_node_gate.gateway_fk_id \
                        INNER JOIN appCode_states_connection ON appCode_states_connection.id = appCode_node_gateway.state_fk_id;")
        nodes_set = cursor.fetchall()
        return nodes_set
    
    def get_nodes_by_gateway(self, gateway_):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_node.ip AS node_ip, appCode_node_gateway.connection_date AS connection_date, appCode_states_connection.name AS state,  \
                        FROM appCode_node_gate INNER JOIN appCode_node ON appCode_node.id = appCode_node_gateway.node_fk_id \
                        INNER JOIN appCode_gateway ON appCode_gateway.id = appCode_node_gateway.gateway_fk_id \
                        INNER JOIN appCode_states_connection ON appCode_states_connection.id = appCode_node_gateway.state_fk_id \
                        WHERE appCode_node_gateway.gateway_fk_id = %s ;", [gateway_])
        nodes_set = cursor.fetchall()
        return nodes_set
    
    def get_nodes_by_gateway_state(self, gateway_, state_):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_node.ip AS node_ip, appCode_node_gateway.connection_date AS connection_date, appCode_states_connection.name AS state,  \
                        FROM appCode_node_gateway INNER JOIN appCode_node ON appCode_node.id = appCode_node_gateway.node_fk_id \
                        INNER JOIN appCode_gateway ON appCode_gateway.id = appCode_node_gateway.gateway_fk_id \
                        INNER JOIN appCode_states_connection ON appCode_states_connection.id = appCode_node_gateway.state_fk_id \
                        WHERE appCode_node_gateway.gateway_fk_id = %s AND appCode_node_gateway.state_fk_id = %s;", [gateway_, state_])
        nodes_set = cursor.fetchall()
        return nodes_set
   
    def insert_node_gateway(self, gateway_, node_, state_, connection_):
        node_gateway = Node_Gateway(gateway_fk = gateway_, node_fk = node_, state_fk = state_, connection = connection_)
        return node_gateway


class Node_Gateway(models.Model):
    gateway_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE, default = 0)
    node_fk = models.ForeignKey(Node, on_delete = models.CASCADE, default = 0)
    state_fk = models.ForeignKey(States_Connection, on_delete = models.CASCADE, default = 0)
    connection_date = models.DateTimeField(auto_now = True)
    node_gateway_manager = Node_Gateway_Manager()



############################# Wifi Model #############################
class Wifi_Protocol_Manager(models.Manager):
    def get_wifi_protocols(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_protocol, name AS name_protocol FROM appCode_wifi_protocol;")
        protocols_set = cursor.fetchall()
        return protocols_set
    
    def insert_wifi_protocol(self, name_, description_):
        protocol = Wifi_Protocol(name = name_, description = description_)
        return protocol


class Wifi_Protocol(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')
    wifi_protocol_manager = Wifi_Protocol_Manager() 



class Wifi_Channel_Manager(models.Manager):
    def get_wifi_channels(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_channel, name AS name_channel FROM appCode_wifi_channel;")
        channels_set = cursor.fetchall()
        return channels_set
    
    def insert_wifi_channel(self, name_, description_):
        channel = Wifi_Channel(name = name_, description = description_)
        return channel


class Wifi_Channel(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')
    wifi_channel_manager = Wifi_Channel_Manager() 



class Wifi(models.Model):
    direction = models.CharField(max_length = 25, default = 'None', unique = True)
    networks_mask = models.CharField(max_length = 25, default = 'None')
    broadcast = models.CharField(max_length = 25, default = 'None')
    dns_1 = models.CharField(max_length = 40, default = 'None')
    dns_2 = models.CharField(max_length = 40, default = 'None')
    protocol = models.ForeignKey(Wifi_Protocol, on_delete = models.CASCADE, default = 0)
    channel = models.ForeignKey(Wifi_Channel, on_delete = models.CASCADE, default = 0)

    def __str__(self):
        return ("Direction: %s\tNetwork Mask: %s\tBroadCast: %s\tDNS 1: %s\tDNS 2: %s\tProtocol: %s\tChannel: %s\n" % (self.direction, self.networks_mask, self.broad_cast, self.dns_1, self.dns_2, self.protocol, self.channel))



class Wifi_Gateway_Manager(models.Manager):
    def get_wifis_gateways(self):
        cursor = connection.cursor()
        cursor.execute("SELECT appCode_wifi.direction AS wifi_direction, appCode_gateway.name AS gateway, appCode_wifi_gateway.connection_date AS connection_date, appCode_states_connection.name AS state,  \
                        FROM appCode_wifi_gateway INNER JOIN appCode_wifi ON appCode_wifi.id = appCode_wifi_gateway.wifi_fk_id \
                        INNER JOIN appCode_gateway ON appCode_gateway.id = appCode_wifi_gateway.gateway_fk_id \
                        INNER JOIN appCode_states_connection ON appCode_states_connection.id = appCode_node_gateway.state_fk_id;")
        nodes_set = cursor.fetchall()
        return nodes_set
    
    def insert_wifi_gateway(self, gateway_, wifi_, state_, connection_):
        wifi_gateway = Wifi_Gateway(gateway_fk = gateway_, wifi_fk = wifi_, state_fk = state_, connection = connection_)
        return wifi_gateway


class Wifi_Gateway(models.Model):
    wifi_fk = models.ForeignKey(Wifi, on_delete = models.CASCADE, default = 0)
    gateway_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE, default = 0)
    state_fk = models.ForeignKey(States_Connection, on_delete = models.CASCADE, default = 0)
    connection_date = models.DateTimeField(auto_now = True)


############################# SimCard Model #############################
class States_Simcard_Manager(models.Manager):
    def get_status_node(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_status, name AS name_status FROM appCode_status_simcard;")
        states_set = cursor.fetchall()
        return states_set
    
    def insert_states_node(self, name_, description_):
        states = States_Simcard(name = name_, description = description_)
        return states


class States_Simcard(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')
    states_simcarf_manager = States_Simcard_Manager()



class Simcard_Operator_Manager(models.Manager):
    def get_simcard_operator(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_operator, name AS name_status FROM appCode_operator_simcard;")
        operators_set = cursor.fetchall()
        return operators_set
    
    def insert_states_node(self, name_, description_):
        operator = Simcard_Operator(name = name_, description = description_)
        return operator


class Simcard_Operator(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')



class Simcard(models.Model):
    name = models.CharField(max_length = 50, default = 'None', unique = True)
    operator_fk = models.ForeignKey(Simcard_Operator, on_delete = models.CASCADE, default = 0)
    card_pin = models.CharField(max_length = 20, default = 'None')
    user_sim = models.CharField(max_length = 30, default = 'None')
    password_sim = models.CharField(max_length = 30, default = 'None')
    state_fk = models.ForeignKey(States_Simcard, on_delete = models.CASCADE, default = 0)
    gateway_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE, default = 0)

    def __str__(self):
        return ("Name: %s\tOperator: %s\tCard PIN: %s\tUser SIM: %s\tPassword SIM: %s\tState: %s\n" % (self.name, self.operator, self.card_pin, self.user_sim, self.password_sim, self.state))




############################# Ethernet Model #############################
class States_Ethernet_Manager(models.Manager):
    def get_states_ethernet(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id AS id_states, name AS name_states FROM appCode_states_ethernet;")
        status_set = cursor.fetchall()
        return status_set
    
    def insert_states_ethernet(self, name_, description_):
        state = States_Ethernet(name = name_, description = description_)
        return state


class States_Ethernet(models.Model):
    name = models.CharField(max_length = 25, default = 'None', unique = True)
    description = models.CharField(max_length = 100, default = 'None')


class Ethernet (models.Model):
    mode = models.CharField(max_length = 20, default = 'None')
    state_fk = models.ForeignKey(States_Ethernet, on_delete = models.CASCADE, default = 0)
    gateway_fk = models.ForeignKey(Gateway, on_delete = models.CASCADE, default = 0)

    def __str__(self):
        return ("Mode: %s\tState: %s\tGateway: %s\n" % (self.mode, self.state_fk, self.gateway_fk))
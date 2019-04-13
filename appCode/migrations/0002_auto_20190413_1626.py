# Generated by Django 2.1.2 on 2019-04-13 21:26

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('appCode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(default='None', max_length=20, unique=True)),
                ('latitude', models.DecimalField(decimal_places=6, default=0.0, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, default=0.0, max_digits=10)),
                ('mac', models.CharField(default='None', max_length=25, unique=True)),
                ('address_16bits', models.CharField(default='None', max_length=30, unique=True)),
            ],
            managers=[
                ('node_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Node_Gateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_date', models.DateTimeField(auto_now=True)),
            ],
            managers=[
                ('node_gateway_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Node_Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('voltage', models.DecimalField(decimal_places=3, default=0.0, max_digits=6)),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('node_fk', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Node')),
            ],
            managers=[
                ('node_register_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Simcard_Operator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=25, unique=True)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='States_Connection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=25, unique=True)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
            managers=[
                ('states_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='States_Ethernet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=25, unique=True)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='States_Gateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=25, unique=True)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
            managers=[
                ('states_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='States_Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=25, unique=True)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
            managers=[
                ('states_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='States_Simcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=25, unique=True)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
            managers=[
                ('states_simcarf_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Wifi_Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=25, unique=True)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
            managers=[
                ('wifi_channel_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Wifi_Gateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('connection_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wifi_Protocol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=25, unique=True)),
                ('description', models.CharField(default='None', max_length=100)),
            ],
            managers=[
                ('wifi_protocol_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='ether_conex_gate',
            name='FK_idEthernet',
        ),
        migrations.RemoveField(
            model_name='ether_conex_gate',
            name='FK_idGateWay',
        ),
        migrations.RemoveField(
            model_name='gate_nodo',
            name='FK_idGateWay',
        ),
        migrations.RemoveField(
            model_name='gate_nodo',
            name='FK_idNodo',
        ),
        migrations.RemoveField(
            model_name='sim_conex_gate',
            name='FK_idGateWay',
        ),
        migrations.RemoveField(
            model_name='sim_conex_gate',
            name='FK_idSimCard',
        ),
        migrations.RemoveField(
            model_name='wifi_conex_gate',
            name='FK_idGateWay',
        ),
        migrations.RemoveField(
            model_name='wifi_conex_gate',
            name='FK_idWifi',
        ),
        migrations.AlterModelManagers(
            name='gateway',
            managers=[
                ('gateways_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='ethernet',
            name='Estado',
        ),
        migrations.RemoveField(
            model_name='ethernet',
            name='ModoConex',
        ),
        migrations.RemoveField(
            model_name='gateway',
            name='Estado',
        ),
        migrations.RemoveField(
            model_name='gateway',
            name='ForeingAddress',
        ),
        migrations.RemoveField(
            model_name='gateway',
            name='LatCoord',
        ),
        migrations.RemoveField(
            model_name='gateway',
            name='LongCoord',
        ),
        migrations.RemoveField(
            model_name='gateway',
            name='Nombre',
        ),
        migrations.RemoveField(
            model_name='gateway',
            name='localAddress',
        ),
        migrations.RemoveField(
            model_name='simcard',
            name='CardPin',
        ),
        migrations.RemoveField(
            model_name='simcard',
            name='Estado',
        ),
        migrations.RemoveField(
            model_name='simcard',
            name='Nombre',
        ),
        migrations.RemoveField(
            model_name='simcard',
            name='Operador',
        ),
        migrations.RemoveField(
            model_name='simcard',
            name='PasswordSim',
        ),
        migrations.RemoveField(
            model_name='simcard',
            name='UserSim',
        ),
        migrations.RemoveField(
            model_name='wifi',
            name='BroadCast',
        ),
        migrations.RemoveField(
            model_name='wifi',
            name='Canal',
        ),
        migrations.RemoveField(
            model_name='wifi',
            name='Direccion',
        ),
        migrations.RemoveField(
            model_name='wifi',
            name='Dns_1',
        ),
        migrations.RemoveField(
            model_name='wifi',
            name='Dns_2',
        ),
        migrations.RemoveField(
            model_name='wifi',
            name='MascaraRed',
        ),
        migrations.RemoveField(
            model_name='wifi',
            name='Protocolo',
        ),
        migrations.AddField(
            model_name='ethernet',
            name='gateway_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Gateway'),
        ),
        migrations.AddField(
            model_name='ethernet',
            name='mode',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='gateway',
            name='foreign_address',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='gateway',
            name='latitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='gateway',
            name='local_address',
            field=models.CharField(default='None', max_length=50),
        ),
        migrations.AddField(
            model_name='gateway',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='gateway',
            name='name',
            field=models.CharField(default='None', max_length=25, unique=True),
        ),
        migrations.AddField(
            model_name='simcard',
            name='card_pin',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='simcard',
            name='gateway_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Gateway'),
        ),
        migrations.AddField(
            model_name='simcard',
            name='name',
            field=models.CharField(default='None', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='simcard',
            name='password_sim',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='simcard',
            name='user_sim',
            field=models.CharField(default='None', max_length=30),
        ),
        migrations.AddField(
            model_name='wifi',
            name='broadcast',
            field=models.CharField(default='None', max_length=25),
        ),
        migrations.AddField(
            model_name='wifi',
            name='direction',
            field=models.CharField(default='None', max_length=25, unique=True),
        ),
        migrations.AddField(
            model_name='wifi',
            name='dns_1',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AddField(
            model_name='wifi',
            name='dns_2',
            field=models.CharField(default='None', max_length=40),
        ),
        migrations.AddField(
            model_name='wifi',
            name='networks_mask',
            field=models.CharField(default='None', max_length=25),
        ),
        migrations.DeleteModel(
            name='Ether_Conex_Gate',
        ),
        migrations.DeleteModel(
            name='Gate_Nodo',
        ),
        migrations.DeleteModel(
            name='Nodo',
        ),
        migrations.DeleteModel(
            name='Sim_Conex_Gate',
        ),
        migrations.DeleteModel(
            name='Wifi_Conex_Gate',
        ),
        migrations.AddField(
            model_name='wifi_gateway',
            name='gateway_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Gateway'),
        ),
        migrations.AddField(
            model_name='wifi_gateway',
            name='state_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.States_Connection'),
        ),
        migrations.AddField(
            model_name='wifi_gateway',
            name='wifi_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Wifi'),
        ),
        migrations.AddField(
            model_name='node_gateway',
            name='gateway_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Gateway'),
        ),
        migrations.AddField(
            model_name='node_gateway',
            name='node_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Node'),
        ),
        migrations.AddField(
            model_name='node_gateway',
            name='state_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.States_Connection'),
        ),
        migrations.AddField(
            model_name='node',
            name='state_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.States_Node'),
        ),
        migrations.AddField(
            model_name='ethernet',
            name='state_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.States_Ethernet'),
        ),
        migrations.AddField(
            model_name='gateway',
            name='state_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.States_Gateway'),
        ),
        migrations.AddField(
            model_name='simcard',
            name='operator_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Simcard_Operator'),
        ),
        migrations.AddField(
            model_name='simcard',
            name='state_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.States_Simcard'),
        ),
        migrations.AddField(
            model_name='wifi',
            name='channel',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Wifi_Channel'),
        ),
        migrations.AddField(
            model_name='wifi',
            name='protocol',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Wifi_Protocol'),
        ),
    ]

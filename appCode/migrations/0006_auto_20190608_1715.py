# Created by L.S. Urrea [lurreaferia@uniminuto.edu.co], J. Sanchez-Rojas [jsanchezro8@uniminuto.edu.co], & C.A.Sierra [carlos.andres.sierra.v@gmail.com] on May 2019.

# Collaboration acknowlegments: María Fernanda Chaparro & Fernando & Santiago Salazar.

# Copyright (c) 2019 L.S. Urrea, J. Sanchez-Rojas, & C.A.Sierra. Research Group on Athenea. All rights reserved.

#

# This file is part of RaspXbee Project.

#

# RaspXbee Project is free software: you can redistribute it and/or modify it under the terms of the

# GNU General Public License as published by the Free Software Foundation, version 3
# Generated by Django 2.1.5 on 2019-06-08 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCode', '0005_auto_20190518_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cauce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('velocidad', models.DecimalField(decimal_places=6, default=0.0, max_digits=10)),
                ('area', models.DecimalField(decimal_places=6, default=0.0, max_digits=10)),
                ('cauce', models.DecimalField(decimal_places=6, default=0.0, max_digits=10)),
                ('lluvia', models.DecimalField(decimal_places=6, default=0.0, max_digits=10)),
                ('fecha', models.DateField()),
                ('status', models.BooleanField(default='None', max_length=25)),
                ('nodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appCode.Node')),
            ],
        ),
        migrations.AlterField(
            model_name='ethernet',
            name='gateway_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Gateway'),
        ),
        migrations.AlterField(
            model_name='node_gateway',
            name='gateway_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Gateway'),
        ),
        migrations.AlterField(
            model_name='simcard',
            name='gateway_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Gateway'),
        ),
        migrations.AlterField(
            model_name='wifi_gateway',
            name='gateway_fk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='appCode.Gateway'),
        ),
    ]

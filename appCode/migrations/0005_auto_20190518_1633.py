# Generated by Django 2.1.5 on 2019-05-18 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appCode', '0004_auto_20190518_1241'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='node',
            managers=[
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

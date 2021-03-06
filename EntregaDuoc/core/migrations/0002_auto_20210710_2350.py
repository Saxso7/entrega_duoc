# Generated by Django 3.2.5 on 2021-07-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('nombre', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('numeroContacto', models.IntegerField(max_length=10, verbose_name='Numero Contacto')),
                ('problemaConsulta', models.CharField(max_length=50, verbose_name='Problema o Consulta')),
                ('correoElectronico', models.CharField(max_length=30, verbose_name='Correo Electronico')),
            ],
        ),
        migrations.AlterField(
            model_name='registro',
            name='contrasenna',
            field=models.CharField(max_length=20, verbose_name='Contraseña'),
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-11 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210710_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='numeroContacto',
            field=models.IntegerField(verbose_name='Numero Contacto'),
        ),
    ]
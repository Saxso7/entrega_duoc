from django.db import models

# Create your models here.


class registro (models.Model):
    correoElectronico = models.CharField(max_length=30, primary_key=True,
    verbose_name='Correo Electronico', unique=True)
    nombreApellido = models.CharField(max_length=40, verbose_name='Nombre y Apellido')
    edad = models.IntegerField(verbose_name='Edad')
    direccion = models.CharField(max_length=40, verbose_name='Direccion')
    contrasenna = models.CharField(max_length=20, verbose_name='Contraseña')


def __str__(self):
    return self.correoElectronico


class contacto (models.Model):
    nombre = models.CharField(max_length=20, primary_key=True,
    verbose_name='Nombre')
    numeroContacto = models.IntegerField(verbose_name='Numero Contacto')
    problemaConsulta = models.CharField(
    max_length=50, verbose_name='Problema o Consulta')
    correoElectronico = models.CharField(
    max_length=30, verbose_name='Correo Electronico')


def __str__(self):
    return self.nombre


class registrarTrabajo(models.Model):
    nombreTrabajo = models.CharField(max_length=30, primary_key=True,
    verbose_name='Nombre Trabajo')
    descripcion = models.CharField(max_length=300, verbose_name='Descripcion')
    costoTrabajo = models.IntegerField(verbose_name='Costo del trabajo')
    fechaTrabajo = models.DateField(verbose_name='Fecha trabajo')


def __str__(self):
    return self.nombreTrabajo

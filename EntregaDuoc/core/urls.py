from django.urls import path
from .views import home,home2, registrar,contacto,inicio_sesion,trabajos,contrasenna_error,trabajos_registrar

urlpatterns = [
    path('',home,name="home"),
    path('home2',home2,name="home2"),
    path('registrar',registrar,name='registrar'),
    path('contacto',contacto,name='contacto'),
    path('inicio_sesion',inicio_sesion,name="inicio_sesion"),
    path('trabajos',trabajos,name="trabajos"),
    path('contrasenna_error',contrasenna_error,name="contrasenna_error"),
    path('registrar_trabajo',trabajos_registrar, name="registrar_trabajo")
]

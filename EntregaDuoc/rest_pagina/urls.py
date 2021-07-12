from django.urls import path
from rest_pagina.views import detalle_registro, lista_registro
from rest_pagina.viewsLogin import login

urlpatterns = [
    path('lista_registros', lista_registro, name="lista_registros"),
    path('detalle_registro/<id>', detalle_registro, name="detalle_registro"),
    path('login', login, name="login"),
]


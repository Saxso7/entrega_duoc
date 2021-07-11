from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import registro, contacto, registrarTrabajo


class registroForm(ModelForm):

    class Meta:
        model = registro
        fields = [
            'correoElectronico',
            'nombreApellido',
            'edad',
            'direccion',
            'contrasenna']


class contactoForm(ModelForm):

    class Meta:
        model = contacto
        fields = ['nombre',
                  'numeroContacto',
                  'problemaConsulta',
                  'correoElectronico']


class registrarTrabajoForm(ModelForm):
    class Meta:
        model = registrarTrabajo
        fields = ['nombreTrabajo',
                  'descripcion',
                  'costoTrabajo',
                  'fechaTrabajo'
                  ]

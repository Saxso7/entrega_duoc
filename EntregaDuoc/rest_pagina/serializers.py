from django.db.models import fields
from rest_framework import serializers
from core.models import registro


class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = registro
        fields = ['correoElectronico', 'nombreApellido',
                  'edad', 'direccion',
                  'contrasenna']


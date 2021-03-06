from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework import decorators
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import registro
from .serializers import RegistroSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))

def lista_registro(request):

    if request.method == 'GET':
        registrar = registro.objects.all()
        serializers = RegistroSerializer(registrar, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = RegistroSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_registro(request, id):

    try:
        registrar = registro.objects.get(correoElectronico=id)
    except registro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RegistroSerializer(registrar)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegistroSerializer(registrar, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        registrar.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

   

# Create your views here.

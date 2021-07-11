from core.forms import registroForm, contactoForm, registrarTrabajoForm
from django.shortcuts import render
from .models import registro, contacto, registrarTrabajo
# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def home2(request):
    return render(request, 'core/home2.html')


def registrar(request):

    datos = {
        'form': registroForm()
    }

    if request.method== 'POST':
        formulario = registroForm(request.POST)
        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/registro.html',datos)


def contacto(request):

    datos = {
        'form': contactoForm()
    }

    if request.method== 'POST':
        formulario = contactoForm(request.POST)
        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Guardado correctamente"

    return render(request, 'core/contacto.html', datos)


def inicio_sesion(request):
    return render(request, 'core/inicio_sesion.html')


def trabajos(request):



    datos = {
        'form': registrarTrabajoForm()
    }

    if request.method== 'POST':
        formulario = registrarTrabajoForm(request.POST)
        if formulario.is_valid:
            formulario.save()

            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'core/trabajos.html', datos)


def contrasenna_error(request):
    return render(request, 'core/contrasenna_error.html')


def trabajo1(request):
    return render(request, 'core/trabajo_cliente_1.html')


def trabajo2(request):
    return render(request, 'core/trabajo_cliente_2.html')


def trabajo3(request):
    return render(request, 'core/trabajo_cliente_3.html')

def trabajos_registrar(request):
    return render(request, 'core/trabajos_registrados.html')
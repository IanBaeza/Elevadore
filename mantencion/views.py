from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from .models import Servicio,Cliente
from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from .forms import ClienteForm, OrdenForm
from .forms import RegistroForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
# Create your views here.

def inicio(request):
    return render(request, 'elev/inicio.html')

def panel(request):
    return render(request, 'elev/panel.html')

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "elev/login.html", {'form': form})

def listaclientes(request):
    cliente = Cliente.objects.all()
    contexto = {'clientes':cliente}
    return render(request, 'elev/listaclientes.html',contexto)

def crearcliente(request):
    if request.method =='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mantencion:success')
    else:
        form = ClienteForm()

        return render(request,'elev/crearcliente.html',{'form':form})

def crearorden(request):
    if request.method =='POST':
        form = OrdenForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mantencion:success')
    else:
        form = OrdenForm()

        return render(request,'elev/crearorden.html',{'form':form})

def success(request):
    return render(request,'elev/success.html')

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
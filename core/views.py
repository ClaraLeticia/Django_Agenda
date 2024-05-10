from django.shortcuts import render, redirect
from core.models import evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def logout_user(request):
    logout(request)
    return redirect('/')


def submit(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
        else:
            messages.error(request, "Usuário ou senha incorretos")

    return redirect('/')


def login_user(request):
    return render(request, 'login.html')


@login_required(login_url='/login/')
def lista_evento(request):
    # usuario = request.user
    # eventos = evento.objects.filter(usuario=usuario)
    eventos = evento.objects.all()
    responce = {'eventos': eventos}
    return render(request, 'agenda.html', responce)

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
def evento_agenda(request):
    return render(request, "evento.html")


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('title')
        descricao = request.POST.get('details')
        data = request.POST.get('date')
        usuario = request.user
        evento.objects.create(titulo=titulo,
                              descricao=descricao,
                              data_evento=data,
                              usuario=usuario)

    return redirect('/')


@login_required(login_url='/login/')
def lista_evento(request):
    usuario = request.user
    eventos = evento.objects.filter(usuario=usuario)
    responce = {'eventos': eventos}
    return render(request, 'agenda.html', responce)

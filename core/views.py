from django.shortcuts import render
from core.models import evento

# Create your views here.


def lista_evento(request):
    eventos = evento.objects.all()
    responce = {'eventos': eventos}
    return render(request, 'agenda.html', responce)
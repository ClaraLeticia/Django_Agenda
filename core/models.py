from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(null=True, blank=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

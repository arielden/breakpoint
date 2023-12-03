# Create your models here.
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Reserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_efectiva = models.DateField()
    fecha_alta = models.DateField(default=date.today)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.fecha_efectiva
# Create your models here.
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Reserva(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_reserva = models.TextField(max_length=10, default="")
    horario_reserva = models.TextField(max_length=5, default="")
    comentario = models.TextField(null=True)
    modificacion = models.DateTimeField(auto_now= True)
    confirma = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.fecha_reserva
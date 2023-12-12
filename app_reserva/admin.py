from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class PartAdmin(admin.ModelAdmin):
    list_display = ['cliente','fecha_reserva','horario_reserva','comentario','modificacion', 'confirma']
    search_fields = ['cliente', 'fecha_reserva']
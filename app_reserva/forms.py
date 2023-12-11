from django.forms import ModelForm
from .models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_reserva',
                  'horario_reserva',
                  'comentario',
                  'confirma'] #Eliminar 'cliente', si se carga automáticamente en la vista.
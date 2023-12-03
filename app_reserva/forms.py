from django.forms import ModelForm
from .models import Reserva

class ReservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['cliente', 
                  'comentario', 
                  'fecha_efectiva',
                  'fecha_alta'] #Eliminar 'resp', si se carga automáticamente en la vista.
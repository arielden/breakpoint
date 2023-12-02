from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class TiendaPage(TemplateView):
    template_name = "tienda.html"

class ReservaPage(TemplateView):
    template_name = "reserva.html"

class ContactoPage(TemplateView):
    template_name = "contacto.html"
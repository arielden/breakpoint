from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = "index.html"

class TiendaPage(TemplateView):
    template_name = "tienda.html"

class ContactoPage(TemplateView):
    template_name = "contacto.html"
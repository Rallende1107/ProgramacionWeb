from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexDosCeroView (TemplateView):
    template_name = 'carrito_dos_punto_cero/index.html'
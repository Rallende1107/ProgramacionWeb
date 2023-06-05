from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexDosView (TemplateView):
    template_name = 'carrito_dos/index.html'
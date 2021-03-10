from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.topiapp.models import Publicacion
from core.topiapp.models import Crear_Usuario
# Create your views here.

def myfirstview(request):
    
    return render(request, 'home.html')
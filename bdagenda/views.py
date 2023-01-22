from django.shortcuts import render
from .models import Contacto #el punto antes de models indica que estan en el directorio actual Esto significa que podemos utilizar "." y el nombre del archivo (sin .py). 

# Create your views here.
def post_list(request):
	contactos = Contacto.objects.all()
	return render(request, 'bdagenda/post_list.html', {'contactos':contactos})
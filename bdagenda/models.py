from django.db import models
# Create your models here.
class Contacto(models.Model):

	nombre = models.CharField(max_length=500)
	correo = models.CharField(max_length=500)
	phonenumb = models.CharField(max_length=500)
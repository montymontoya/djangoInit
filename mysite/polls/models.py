from django.db import models

class impresiones3d (models.Model):
    nombre = models.CharField(max_length=20)
    gramaje = models.CharField(max_length=10)
    tiempo = models.CharField(max_length=10)
    cantidad = models.CharField(max_length=10)
    filamento = models.CharField(max_length=40)
    picture = models.ImageField(upload_to='media/uploads')



from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False)
    deshabilitado = models.BooleanField(default=False, blank=True)    

    def __str__(self):
        return str(self.nombre)
    
    class Meta:
        ordering = ['nombre']


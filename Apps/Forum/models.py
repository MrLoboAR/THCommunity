from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Nuevo Hilo')
    content = models.TextField(verbose_name='Descripcion')
    c_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion:')

    def __str__(self):
        return f'Thread: {self.title}| Uploaded Date: {self.c_date}'
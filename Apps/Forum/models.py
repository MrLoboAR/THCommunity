from tabnanny import verbose
from django.db import models

# Tuples

STATUS_CHOICES = (
    ('R', "Reviewed"),
    ('E', "Error"),
    ('N', 'Not Reviewed'),
    ('A', 'Accepted'),
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Nuevo Hilo')
    content = models.TextField(verbose_name='Descripcion')
    c_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion:')
    edit = models.IntegerField(default=0)

    class Meta:
        ordering = ['-c_date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'Thread: {self.title}| Uploaded Date: {self.c_date}'

class User(models.Model):
    username = models.CharField('nombre de usuario',max_length=12, unique=True,)
    name = models.CharField('Nombre',max_length=16)
    singup_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-singup_date']
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f'{self.username} | Nombre: {self.name} | Fecha de registro: {self.singup_date}'

class WebSite(models.Model):
    name = models.CharField('nombre',max_length=20)
    url = models.URLField('direccion url',unique=True)
    relase_date = models.DateField(auto_now_add=True)
    rating = models.IntegerField()
    status = models.CharField('estado del sitio',max_length=1, choices=STATUS_CHOICES)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name='Creador de la pagina')

    class Meta:
        ordering = ['-rating']
        verbose_name = 'Una Pagina Web'
        verbose_name_plural = 'Paginas Web'

    def __str__(self):
        owner = self.owner.name
        owner_aka = self.owner.username
        stus = self.get_status_display()
        return f"{self.url} | nombre = {self.name} | Rate: {self.rating}/100 | Creador: {owner} - {owner_aka} | Estatus: {stus}  | Relased {self.relase_date} |"
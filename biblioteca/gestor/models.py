from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    año_publicacion = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    numero_identificacion = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField()

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.usuario.nombre}"


from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    numero_identificacion = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    año_publicacion = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="prestamos")
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="prestamos")
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.usuario.nombre}"

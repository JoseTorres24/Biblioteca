from django.shortcuts import render
from .models import Libro, Prestamo
from datetime import date, timedelta

def listar_libros(request):
    libros = Libro.objects.filter(disponible=True)
    return render(request, "gestor/listar_libros.html", {"libros": libros})

def listar_prestamos(request):
    prestamos = Prestamo.objects.all()
    return render(request, "gestor/listar_prestamos.html", {"prestamos": prestamos})

def notificacion_vencimiento():
    hoy = date.today()
    return Prestamo.objects.filter(fecha_devolucion__lte=hoy + timedelta(days=2))

def menu(request):
    return render(request, "gestor/menu.html")

def registrar_libro(request):
    return render(request, "gestor/registrar_libro.html")

def registrar_usuario(request):
    return render(request, "gestor/registrar_usuario.html")


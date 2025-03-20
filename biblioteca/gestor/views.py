from django.shortcuts import redirect, render,get_object_or_404
from .models import Libro, Prestamo, Usuario
from datetime import date, timedelta

def listar_libros(request):
    libros = Libro.objects.filter(disponible=True)
    return render(request, "gestor/listar_libros.html", {"libros": libros})

def listar_prestamos(request):
    if request.method == "POST":
        usuario_id = request.POST.get("usuario")
        libro_id = request.POST.get("libro")

        if usuario_id and libro_id:
            usuario = Usuario.objects.get(id=usuario_id)
            libro = Libro.objects.get(id=libro_id)

            # Marcar el libro como no disponible
            libro.disponible = False
            libro.save()

            # Crear el préstamo con fecha de devolución en 7 días
            Prestamo.objects.create(
                usuario=usuario,
                libro=libro,
                fecha_prestamo=date.today(),
                fecha_devolucion=date.today() + timedelta(days=7)
            )

            return redirect("listar_prestamos")  # Redirige para evitar reenvíos

    # Obtener datos para mostrar en la vista
    prestamos = Prestamo.objects.all()
    usuarios = Usuario.objects.all()
    libros_disponibles = Libro.objects.filter(disponible=True)

    return render(
        request,
        "gestor/listar_prestamos.html",
        {"prestamos": prestamos, "usuarios": usuarios, "libros": libros_disponibles}
    )

def devolver_libro(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, id=prestamo_id)

    # Marcar el libro como disponible nuevamente
    prestamo.libro.disponible = True
    prestamo.libro.save()
    # Eliminar el préstamo
    prestamo.delete()

    return redirect("listar_prestamos")  # Redirige a la lista de préstamos
def notificacion_vencimiento():
    hoy = date.today()
    return Prestamo.objects.filter(fecha_devolucion__lte=hoy + timedelta(days=2))

def menu(request):
    return render(request, "gestor/menu.html")

from django.shortcuts import render, redirect
from .models import Libro

def registrar_libro(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo")
        autor = request.POST.get("autor")
        genero = request.POST.get("genero")
        año_publicacion = request.POST.get("año_publicacion")
        disponible = request.POST.get("disponible") == "on"  # Convierte checkbox en booleano

        if titulo and autor and genero and año_publicacion:
            Libro.objects.create(
                titulo=titulo,
                autor=autor,
                genero=genero,
                año_publicacion=año_publicacion,
                disponible=disponible
            )
            return redirect("menu")  # Redirige al menú después de registrar el libro

    return render(request, "gestor/registrar_libro.html")


def registrar_usuario(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        numero_identificacion = request.POST.get("numero_identificacion")

        if nombre and email and numero_identificacion:  # Validación básica
            Usuario.objects.create(nombre=nombre, email=email, numero_identificacion=numero_identificacion)
            return redirect("menu")  # Redirigir al menu

    return render(request, "gestor/registrar_usuario.html")


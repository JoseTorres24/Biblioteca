from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuario, Libro, Prestamo
from .forms import LibroForm, UsuarioForm, PrestamoForm

# Menú Principal
def menu(request):
    return render(request, 'gestor/menu.html')

# Listar Libros
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'gestor/listar_libros.html', {'libros': libros})

# Registrar Libro
def registrar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()
    return render(request, 'gestor/registrar_libro.html', {'form': form})

# Registrar Usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = UsuarioForm()
    return render(request, 'gestor/registrar_usuario.html', {'form': form})

# Listar Préstamos
def listar_prestamos(request):
    prestamos = Prestamo.objects.select_related('usuario', 'libro').all()
    usuarios = Usuario.objects.all()
    libros = Libro.objects.filter(disponible=True)

    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save()
            prestamo.libro.disponible = False
            prestamo.libro.save()
            return redirect('listar_prestamos')
    else:
        form = PrestamoForm()

    return render(request, 'gestor/listar_prestamos.html', {
        'prestamos': prestamos,
        'usuarios': usuarios,
        'libros': libros,
        'form': form,
    })

# Devolver Libro
def devolver_libro(request, prestamo_id):
    prestamo = Prestamo.objects.get(id=prestamo_id)
    prestamo.libro.disponible = True
    prestamo.libro.save()
    prestamo.delete()
    return redirect('listar_prestamos')

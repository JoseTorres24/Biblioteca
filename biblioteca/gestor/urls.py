from django.urls import path
from .views import devolver_libro, menu, listar_libros, registrar_libro, registrar_usuario, listar_prestamos

urlpatterns = [
    path("", menu, name="menu"),
    path("libros/", listar_libros, name="listar_libros"),
    path("libros/nuevo/", registrar_libro, name="registrar_libro"),
    path("usuarios/nuevo/", registrar_usuario, name="registrar_usuario"),
    path("prestamos/", listar_prestamos, name="listar_prestamos"),
    path("prestamos/devolver/<int:prestamo_id>/", devolver_libro, name="devolver_libro"),
]

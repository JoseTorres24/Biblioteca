from django.contrib import admin
from .models import Libro, Usuario, Prestamo

admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Prestamo)


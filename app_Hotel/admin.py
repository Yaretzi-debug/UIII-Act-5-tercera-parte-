from django.contrib import admin
from .models import Empleado, Huesped, Habitacion

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cargo', 'salario', 'turno', 'telefono')
    list_filter = ('cargo', 'turno')
    search_fields = ('nombre', 'apellido')

@admin.register(Huesped)
class HuespedAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'telefono', 'email', 'fecha_registro', 'registrado_por')
    list_filter = ('fecha_registro',)
    search_fields = ('nombre', 'apellido', 'email')
    filter_horizontal = ('habitaciones',)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'capacidad', 'precio_por_noche', 'disponibles', 'piso', 'estado_limpieza')
    list_filter = ('tipo', 'disponibles', 'piso', 'estado_limpieza')
    search_fields = ('numero',)
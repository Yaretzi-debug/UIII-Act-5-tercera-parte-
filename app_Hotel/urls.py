from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_hotel, name='inicio_hotel'),
    
    # Empleados
    path('empleados/agregar/', views.agregar_empleados, name='agregar_empleados'),
    path('empleados/ver/', views.ver_empleados, name='ver_empleados'),
    path('empleados/actualizar/', views.actualizar_empleados, name='actualizar_empleados'),
    path('empleados/actualizar/<int:empleado_id>/', views.realizar_actualizacion_empleados, name='realizar_actualizacion_empleados'),
    path('empleados/borrar/', views.borrar_empleados, name='borrar_empleados'),
    path('empleados/borrar/<int:empleado_id>/', views.realizar_borrado_empleados, name='realizar_borrado_empleados'),
    
    # Huéspedes
    path('huespedes/agregar/', views.agregar_huesped, name='agregar_huesped'),
    path('huespedes/ver/', views.ver_huespedes, name='ver_huespedes'),
    path('huespedes/actualizar/', views.actualizar_huesped, name='actualizar_huesped'),
    path('huespedes/actualizar/<int:huesped_id>/', views.realizar_actualizacion_huesped, name='realizar_actualizacion_huesped'),
    path('huespedes/borrar/', views.borrar_huesped, name='borrar_huesped'),
    path('huespedes/borrar/<int:huesped_id>/', views.realizar_borrado_huesped, name='realizar_borrado_huesped'),
    
    # Habitaciones
    path('habitaciones/agregar/', views.agregar_habitacion, name='agregar_habitacion'),
    path('habitaciones/ver/', views.ver_habitaciones, name='ver_habitaciones'),
    path('habitaciones/actualizar/', views.actualizar_habitacion, name='actualizar_habitacion'),
    path('habitaciones/actualizar/<int:habitacion_id>/', views.realizar_actualizacion_habitacion, name='realizar_actualizacion_habitacion'),
    path('habitaciones/borrar/', views.borrar_habitacion, name='borrar_habitacion'),
    path('habitaciones/borrar/<int:habitacion_id>/', views.realizar_borrado_habitacion, name='realizar_borrado_habitacion'),
]
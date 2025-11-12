from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import Empleado, Huesped, Habitacion

def inicio_hotel(request):
    return render(request, 'inicio.html')

# Vistas para Empleados
def agregar_empleados(request):
    if request.method == 'POST':
        empleado = Empleado(
            nombre=request.POST['nombre'],
            apellido=request.POST['apellido'],
            cargo=request.POST['cargo'],
            fecha_contratacion=request.POST['fecha_contratacion'],
            salario=request.POST['salario'],
            turno=request.POST['turno'],
            telefono=request.POST['telefono']
        )
        empleado.save()
        return redirect('ver_empleados')
    
    return render(request, 'empleados/agregar_empleados.html')

def ver_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/ver_empleados.html', {'empleados': empleados})

def actualizar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/actualizar_empleados.html', {'empleados': empleados})

def realizar_actualizacion_empleados(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    
    if request.method == 'POST':
        empleado.nombre = request.POST['nombre']
        empleado.apellido = request.POST['apellido']
        empleado.cargo = request.POST['cargo']
        empleado.fecha_contratacion = request.POST['fecha_contratacion']
        empleado.salario = request.POST['salario']
        empleado.turno = request.POST['turno']
        empleado.telefono = request.POST['telefono']
        empleado.save()
        return redirect('ver_empleados')
    
    return render(request, 'empleados/actualizar_empleados_form.html', {'empleado': empleado})

def borrar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/borrar_empleados.html', {'empleados': empleados})

def realizar_borrado_empleados(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('ver_empleados')
    
    return render(request, 'empleados/confirmar_borrado.html', {'empleado': empleado})

# Vistas para Huéspedes
def agregar_huesped(request):
    if request.method == 'POST':
        email = request.POST['email']
        
        # Verificar si el email ya existe
        if Huesped.objects.filter(email=email).exists():
            mensaje_error = "El email ya está registrado. Por favor, use un email diferente."
            empleados = Empleado.objects.all()
            habitaciones = Habitacion.objects.filter(disponibles=True)
            return render(request, 'huespedes/agregar_huesped.html', {
                'empleados': empleados,
                'habitaciones': habitaciones,
                'error_message': mensaje_error,
                'form_data': request.POST
            })
        
        try:
            # Obtener el empleado que registra (puede ser None)
            empleado_id = request.POST.get('registrado_por')
            empleado = None
            if empleado_id and empleado_id != '':
                empleado = Empleado.objects.get(id=empleado_id)
            
            # Crear nuevo huésped
            huesped = Huesped(
                nombre=request.POST['nombre'],
                apellido=request.POST['apellido'],
                telefono=request.POST['telefono'],
                email=email,
                direccion=request.POST['direccion'],
                registrado_por=empleado
            )
            huesped.save()
            
            # Procesar habitaciones si se seleccionaron
            habitaciones_ids = request.POST.getlist('habitaciones')
            if habitaciones_ids:
                habitaciones = Habitacion.objects.filter(id__in=habitaciones_ids)
                huesped.habitaciones.set(habitaciones)
            
            return redirect('ver_huespedes')
        
        except IntegrityError:
            # Manejar el error de email duplicado
            mensaje_error = "El email ya está registrado. Por favor, use un email diferente."
            empleados = Empleado.objects.all()
            habitaciones = Habitacion.objects.filter(disponibles=True)
            return render(request, 'huespedes/agregar_huesped.html', {
                'empleados': empleados,
                'habitaciones': habitaciones,
                'error_message': mensaje_error,
                'form_data': request.POST
            })
        except Exception as e:
            # Manejar otros posibles errores
            mensaje_error = f"Error al guardar el huésped: {str(e)}"
            empleados = Empleado.objects.all()
            habitaciones = Habitacion.objects.filter(disponibles=True)
            return render(request, 'huespedes/agregar_huesped.html', {
                'empleados': empleados,
                'habitaciones': habitaciones,
                'error_message': mensaje_error,
                'form_data': request.POST
            })
    
    empleados = Empleado.objects.all()
    habitaciones = Habitacion.objects.filter(disponibles=True)
    return render(request, 'huespedes/agregar_huesped.html', {
        'empleados': empleados,
        'habitaciones': habitaciones
    })

def ver_huespedes(request):
    huespedes = Huesped.objects.all()
    return render(request, 'huespedes/ver_huespedes.html', {'huespedes': huespedes})

def actualizar_huesped(request):
    huespedes = Huesped.objects.all()
    return render(request, 'huespedes/actualizar_huesped.html', {'huespedes': huespedes})

def realizar_actualizacion_huesped(request, huesped_id):
    huesped = get_object_or_404(Huesped, id=huesped_id)
    
    if request.method == 'POST':
        huesped.nombre = request.POST['nombre']
        huesped.apellido = request.POST['apellido']
        huesped.telefono = request.POST['telefono']
        huesped.email = request.POST['email']
        huesped.direccion = request.POST['direccion']
        
        # Actualizar empleado que registró
        empleado_id = request.POST.get('registrado_por')
        if empleado_id and empleado_id != '':
            huesped.registrado_por = Empleado.objects.get(id=empleado_id)
        else:
            huesped.registrado_por = None
        
        huesped.save()
        
        # Actualizar habitaciones
        habitaciones_ids = request.POST.getlist('habitaciones')
        habitaciones = Habitacion.objects.filter(id__in=habitaciones_ids)
        huesped.habitaciones.set(habitaciones)
        
        return redirect('ver_huespedes')
    
    empleados = Empleado.objects.all()
    habitaciones = Habitacion.objects.filter(disponibles=True)
    return render(request, 'huespedes/actualizar_huesped_form.html', {
        'huesped': huesped,
        'empleados': empleados,
        'habitaciones': habitaciones
    })

def borrar_huesped(request):
    huespedes = Huesped.objects.all()
    return render(request, 'huespedes/borrar_huesped.html', {'huespedes': huespedes})

def realizar_borrado_huesped(request, huesped_id):
    huesped = get_object_or_404(Huesped, id=huesped_id)
    
    if request.method == 'POST':
        huesped.delete()
        return redirect('ver_huespedes')
    
    return render(request, 'huespedes/confirmar_borrado_huesped.html', {'huesped': huesped})

# Vistas para Habitaciones (CORREGIDAS)
def agregar_habitacion(request):
    if request.method == 'POST':
        # Crear nueva habitación
        habitacion = Habitacion(
            numero=request.POST['numero'],
            tipo=request.POST['tipo'],
            capacidad=request.POST['capacidad'],
            precio_por_noche=request.POST['precio_por_noche'],
            disponibles='disponibles' in request.POST,  # CORREGIDO
            piso=request.POST['piso'],
            estado_limpieza=request.POST['estado_limpieza']
        )
        habitacion.save()
        return redirect('ver_habitaciones')
    
    return render(request, 'habitacion/agregar_habitacion.html')

def ver_habitaciones(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitacion/ver_habitaciones.html', {'habitaciones': habitaciones})

def actualizar_habitacion(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitacion/actualizar_habitacion.html', {'habitaciones': habitaciones})

def realizar_actualizacion_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    
    if request.method == 'POST':
        habitacion.numero = request.POST['numero']
        habitacion.tipo = request.POST['tipo']
        habitacion.capacidad = request.POST['capacidad']
        habitacion.precio_por_noche = request.POST['precio_por_noche']
        habitacion.disponibles = 'disponibles' in request.POST  # CORREGIDO
        habitacion.piso = request.POST['piso']
        habitacion.estado_limpieza = request.POST['estado_limpieza']
        habitacion.save()
        return redirect('ver_habitaciones')
    
    return render(request, 'habitacion/actualizar_habitacion_form.html', {'habitacion': habitacion})

def borrar_habitacion(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'habitacion/borrar_habitacion.html', {'habitaciones': habitaciones})

def realizar_borrado_habitacion(request, habitacion_id):
    habitacion = get_object_or_404(Habitacion, id=habitacion_id)
    
    if request.method == 'POST':
        habitacion.delete()
        return redirect('ver_habitaciones')
    
    return render(request, 'habitacion/confirmar_borrado_habitacion.html', {'habitacion': habitacion})
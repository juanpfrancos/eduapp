from django.contrib.auth.decorators import user_passes_test
from django.utils.datetime_safe import datetime
from django.shortcuts import render, redirect
from .forms import RegistroForm
from .models import Registro


@user_passes_test(lambda u: u.is_authenticated and u.role == 'user', login_url='/')
def crear_registro(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['empleado'] = request.user.name
        form = RegistroForm(form_data)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.empleado = request.user.name
            registro.save()
            return redirect('lista_registros')
        else:
            print(form.errors)
    else:
        form = RegistroForm()
    return render(request, 'crear_registro.html', {'form': form})



def lista_registros(request):
    registros = Registro.objects.all()
    fechas = Registro.objects.values_list('fecha', flat=True).distinct()
    empleados = Registro.objects.values_list('empleado', flat=True).distinct()

    fecha_filtro = request.GET.get('fecha_filtro')
    empleado_filtro = request.GET.get('empleado_filtro')

    if fecha_filtro:
        fecha_filtro = datetime.strptime(fecha_filtro, '%Y-%m-%d')  # Parsear la fecha
        registros = registros.filter(fecha=fecha_filtro)
    if empleado_filtro:
        registros = registros.filter(empleado=empleado_filtro)

    return render(request, 'lista_registros.html', {
        'registros': registros,
        'fechas': fechas,
        'empleados': empleados,
    })

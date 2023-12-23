from django.views.generic import View

from django.core.mail import EmailMessage
from io import BytesIO
from django.contrib.auth.decorators import user_passes_test
from django.utils.datetime_safe import datetime
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistroForm
from .models import Registro
from json import dumps 
from datetime import datetime
from decouple import config
import pandas as pd


@user_passes_test(lambda u: u.is_authenticated and u.role == 'user', login_url='/')
def crear_registro(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['empleado'] = request.user.name
        form = RegistroForm(form_data)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.empleado = request.user
            registro.save()
            return redirect('lista_registros')
        else:
            print(form.errors)
    else:
        form = RegistroForm()
    return render(request, 'crear_registro.html', {'form': form})


@user_passes_test(lambda u: u.is_authenticated and u.role == 'admin', login_url='/')
def lista_registros(request):
    admin_school = request.user.school
    registros = Registro.objects.filter(empleado__school=admin_school)
    fechas = registros.values_list('fecha', flat=True).distinct()
    empleados = registros.values_list('empleado__id', 'empleado__name').distinct()

    fecha_filtro = request.GET.get('fecha_filtro')
    empleado_filtro = request.GET.get('empleado_filtro')

    if fecha_filtro:
        fecha_filtro = datetime.strptime(fecha_filtro, '%Y-%m-%d')  # Parsear la fecha
        registros = registros.filter(fecha=fecha_filtro)
    if empleado_filtro:
        registros = registros.filter(empleado=empleado_filtro)
    data = list(registros.values())
    registros = list(map(lambda item: {**item, 'fecha': item['fecha'].strftime('%Y-%m-%d')}, data))
    final = [{key: str(value) for key, value in data.items()} for data in registros]
    return render(request, 'lista_registros.html', {
        'registros': dumps(final),
        'fechas': fechas,
        'empleados': empleados,
    })





@user_passes_test(lambda u: u.is_authenticated and u.role == 'admin', login_url='/')
def send_email_view(request):
    try:
        admin_school = request.user.school
        registros = Registro.objects.filter(empleado__school=admin_school)

        fecha_filtro = request.GET.get('fecha_filtro')
        empleado_filtro = request.GET.get('empleado_filtro')

        filters = {}
        if fecha_filtro:
            filters['fecha'] = datetime.strptime(fecha_filtro, '%Y-%m-%d')
        if empleado_filtro:
            filters['empleado'] = empleado_filtro

        registros = registros.filter(**filters)

        data = list(registros.values())
        registros = [{**item, 'fecha': item['fecha'].strftime('%Y-%m-%d')} for item in data]
        final = [{key: str(value) for key, value in item.items()} for item in registros]
        file_ = create_xlsx(final)

        subject = 'Entradas y salidas'
        body = 'Archivo adjunto'
        email = EmailMessage(subject, body, None, ['j.franco4@utp.edu.co'])
        email.attach('entradas-salidas.xlsx', file_, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        email.send()
        return HttpResponse('Correo enviado')

    except ValueError as e:
        return HttpResponse(f'Error al parsear la fecha: {str(e)}')
    except Exception as e:
        return HttpResponse(f'Ocurrió un error: {str(e)}')



def create_xlsx(data):
    df = pd.DataFrame.from_records(data)
    with BytesIO() as excel_file:
        df.to_excel(excel_file, index=False)
        excel_file.seek(0)
        excel = excel_file.read()
    return excel

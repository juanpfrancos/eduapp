from django.views.generic import View
from django.core.mail import EmailMessage
from io import BytesIO
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistroForm
from .models import Registro
from datetime import datetime
import pandas as pd


@user_passes_test(lambda u: u.is_authenticated and u.role == 'teacher', login_url='/')
def crear_registro(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        form_data['employee'] = request.user.name
        form = RegistroForm(form_data)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.employee = request.user
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
    registros = Registro.objects.filter(employee__school=admin_school)
    dates = registros.values_list('date', flat=True).distinct()
    employees = registros.values_list('employee__id', 'employee__name').distinct()

    date_filtro = request.GET.get('date_filter')
    employee_filtro = request.GET.get('employee_filter')

    if date_filtro:
        date_filtro = datetime.strptime(date_filtro, '%Y-%m-%d')  # Parsear la date
        registros = registros.filter(date=date_filtro)
    if employee_filtro:
        registros = registros.filter(employee=employee_filtro)
    data = list(registros.values())
    registros = list(map(lambda item: {**item, 'date': item['date'].strftime('%Y-%m-%d')}, data))
    final = [{key: str(value) for key, value in data.items()} for data in registros]
    print(employees.all)
    return render(request, 'swiper.html', {
        'registros': final,
        'dates': dates,
        'employees': employees,
    })





@user_passes_test(lambda u: u.is_authenticated and u.role == 'admin', login_url='/')
def send_email_view(request):
    try:
        admin_school = request.user.school
        registros = Registro.objects.filter(employee__school=admin_school)

        date_filtro = request.GET.get('date_filtro')
        employee_filtro = request.GET.get('employee_filtro')

        filters = {}
        if date_filtro:
            filters['date'] = datetime.strptime(date_filtro, '%Y-%m-%d')
        if employee_filtro:
            filters['employee'] = employee_filtro

        registros = registros.filter(**filters)

        data = list(registros.values())
        registros = [{**item, 'date': item['date'].strftime('%Y-%m-%d')} for item in data]
        final = [{key: str(value) for key, value in item.items()} for item in registros]
        file_ = create_xlsx(final)

        subject = 'Entradas y salidas'
        body = 'Archivo adjunto'
        email = EmailMessage(subject, body, None, ['j.franco4@utp.edu.co'])
        email.attach('entradas-salidas.xlsx', file_, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        email.send()
        return HttpResponse('Correo enviado')

    except ValueError as e:
        return HttpResponse(f'Error al parsear la date: {str(e)}')
    except Exception as e:
        return HttpResponse(f'Ocurrió un error: {str(e)}')



def create_xlsx(data):
    df = pd.DataFrame.from_records(data)
    with BytesIO() as excel_file:
        df.to_excel(excel_file, index=False)
        excel_file.seek(0)
        excel = excel_file.read()
    return excel

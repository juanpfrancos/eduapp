from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from ..models import Student, Observations
from ..forms import StudentForm
from decouple import config
import requests
from PIL import Image
import io

ENDPOINT = config('BUCKET_ENDPOINT')

@user_passes_test(lambda u: (u.is_authenticated and u.role == 'teacher') or (u.is_authenticated and u.role == 'admin'), login_url='/')
def student_list(request):
    user_school = request.user.school
    students = Student.objects.filter(school=user_school)
    return render(request, 'student_list.html', {'students': students})


@user_passes_test(lambda u: (u.is_authenticated and u.role == 'teacher') or (u.is_authenticated and u.role == 'admin'), login_url='/')
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    observations = Observations.objects.filter(student=student)
    return render(request, 'student_detail.html', {'student': student, 'observations': observations, 'endpoint': ENDPOINT})


@user_passes_test(lambda u: (u.is_authenticated and u.role == 'teacher') or (u.is_authenticated and u.role == 'admin'), login_url='/')
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            up_image(request.user.school, student.pk, form.cleaned_data['temporary_photo'].file)
            return redirect('student_detail', pk=student.pk)
        else:
            print(form.errors)
    else:
        choices = [(request.user.school.id, request.user.school)]
        form = StudentForm(initial={'school': request.user.school})
        form.fields['school'].widget.choices = choices
        form.fields['school'].initial = request.user.school
        form.fields['school'].widget.attrs['readonly'] = True
    return render(request, 'student_form.html', {'form': form})


@user_passes_test(lambda u: (u.is_authenticated and u.role == 'teacher') or (u.is_authenticated and u.role == 'admin'), login_url='/')
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            up_image(request.user.school, student.pk, form.cleaned_data['temporary_photo'].file)
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})


@user_passes_test(lambda u: (u.is_authenticated and u.role == 'teacher') or (u.is_authenticated and u.role == 'admin'), login_url='/')
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')


def up_image(school,id,file):
    url = f"{ENDPOINT}/{school}/{id}.webp"
    headers = {
    'Content-Type': 'image/webp'
    }

    image = resize_image(file)
    response = requests.request("PUT", url, headers=headers, data=image)
    return response.status_code

def resize_image(file):
    output_bytes = io.BytesIO()
    image = Image.open(file)
    image = image.resize((500, 500), Image.BILINEAR)
    image.save(output_bytes, 'WEBP', quality=80, optimize=True)
    return output_bytes.getvalue()

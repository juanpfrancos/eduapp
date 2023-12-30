from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from students.models import Student
from .models import Attendance
from .forms import AttendanceForm
from datetime import datetime
from django.utils import timezone


@user_passes_test(lambda u: (u.is_authenticated and u.role == 'teacher') or (u.is_authenticated and u.role == 'admin'), login_url='/')
def mark_attendance(request):
    user_school = request.user.school
    students = Student.objects.filter(school=user_school)  
    if request.method == 'POST':
        for student in students:
            attended = request.POST.get(str(student.id))
            Attendance.objects.update_or_create(
                student=student,
                date=timezone.now().date(),
                defaults={'attended': attended == 'on'}
            )
        return redirect('attendance_list')

    form = AttendanceForm()

    return render(request, 'mark_attendance.html', {'students': students, 'form': form})

@user_passes_test(lambda u: (u.is_authenticated and u.role == 'teacher') or (u.is_authenticated and u.role == 'admin'), login_url='/')
def attendance_list(request):
    if request.method == 'POST' and request.POST.get('date'):
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        attendances = Attendance.objects.filter(date=date, attended=True)
    else:
        attendances = Attendance.objects.filter(attended=True)

    return render(request, 'attendance_list.html', {'attendances': attendances})

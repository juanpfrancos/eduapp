from django.shortcuts import render, get_object_or_404, redirect
from students.models import Student
from .models import Attendance
from .forms import AttendanceForm
from datetime import datetime
from django.utils import timezone


def mark_attendance(request):
    students = Student.objects.all()
    
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


def attendance_list(request):
    if request.method == 'POST' and request.POST.get('date'):
        date_str = request.POST.get('date')
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        attendances = Attendance.objects.filter(date=date, attended=True)
    else:
        attendances = Attendance.objects.filter(attended=True)

    return render(request, 'attendance_list.html', {'attendances': attendances})

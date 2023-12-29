from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from ..models import Student
from ..forms import ObservationsForm


@user_passes_test(lambda u: (u.is_authenticated and u.role == 'teacher') or (u.is_authenticated and u.role == 'admin'), login_url='/')
def add_observation(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = ObservationsForm(request.POST)
        if form.is_valid():
            observation = form.save(commit=False)
            observation.student = student
            observation.save()
            return redirect('student_detail', pk=student_id)
    else:
        form = ObservationsForm()

    return render(request, 'add_observation.html', {'form': form, 'student': student})

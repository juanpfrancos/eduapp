from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import SchoolForm
from .models import School


@user_passes_test(lambda u: u.is_authenticated and u.role == 'supadmin', login_url='/')
def school_list(request):
    schools = School.objects.all()
    return render(request, 'school_list.html', {'schools': schools})


@user_passes_test(lambda u: u.is_authenticated and u.role == 'supadmin', login_url='/')
def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm()
    return render(request, 'add_school.html', {'form': form})

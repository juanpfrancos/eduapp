from django.shortcuts import render, redirect
from .forms import SchoolForm
from .models import School

def school_list(request):
    schools = School.objects.all()
    return render(request, 'school_list.html', {'schools': schools})

def add_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_list')
    else:
        form = SchoolForm()
    return render(request, 'add_school.html', {'form': form})

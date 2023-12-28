from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from ..forms import RegistrationForm, LoginForm

@user_passes_test(lambda u: u.is_authenticated and u.role == 'supadmin', login_url='/')
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.user.is_authenticated:
        if request.user.role == 'user':
            return redirect('user')
        elif request.user.role == 'admin':
            return redirect('admin')

    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.role == 'user':
                return redirect('user')
            elif user.role == 'admin':
                return redirect('admin')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


@user_passes_test(lambda u: u.is_authenticated and u.role == 'user', login_url='/')
def user_role(request):
    user = request.user
    context = {
        'username': user.name,
        'email': user.email,
        'role': user.role,
    }
    return render(request, 'home/user.html', context)


@user_passes_test(lambda u: u.is_authenticated and u.role == 'admin', login_url='/')
def admin_role(request):
    user = request.user
    context = {
        'username': user.name,
        'email': user.email,
        'role': user.role,
        'school': user.school.name_school if user.school else 'No school assigned',
    }
    return render(request, 'home/admin.html', context)
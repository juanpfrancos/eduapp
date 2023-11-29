from django.urls import path
from . import views

urlpatterns = [
    path('school_list/', views.school_list, name='school_list'),
    path('add_school/', views.add_school, name='add_school'),
]

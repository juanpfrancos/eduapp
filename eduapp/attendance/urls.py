from django.urls import path
from .views import mark_attendance, attendance_list

urlpatterns = [
    path('mark-attendance/', mark_attendance, name='mark_attendance'),
    path('attendance-list/', attendance_list, name='attendance_list'),
]

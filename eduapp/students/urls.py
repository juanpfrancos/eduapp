from django.urls import path
from .views.student_views import student_list, student_detail, student_create, student_update, student_delete
from .views.observation_views import add_observation


urlpatterns = [
    path('students/<int:student_id>/add_observation/', add_observation, name='add_observation'),
    path('students/', student_list, name='student_list'),
    path('students/<int:pk>/', student_detail, name='student_detail'),
    path('students/create/', student_create, name='student_create'),
    path('students/<int:pk>/update/', student_update, name='student_update'),
    path('students/<int:pk>/delete/', student_delete, name='student_delete'),
]

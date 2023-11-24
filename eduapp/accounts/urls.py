from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import logreg
from .views import reset

reset_patterns = [
    path('', reset.CustomPasswordResetView.as_view(), name='password_reset'),
    path('done/', auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'), name='password_reset_complete'),
]

urlpatterns = [
    path('', logreg.user_login, name='login'),
    path('register/', logreg.register, name='register'),
    path('logout/', logreg.user_logout, name='logout'),
    path('admin/', logreg.admin_role, name='admin'),
    path('user/', logreg.user_role, name='user'),
    path('reset/', include(reset_patterns)),
]


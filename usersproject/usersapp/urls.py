from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import logreg_views
from . import reset_views

reset_patterns = [
    path('', reset_views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('done/', auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_done.html'), name='password_reset_done'),
    path('confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('complete/', auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'), name='password_reset_complete'),
]

urlpatterns = [
    path('', logreg_views.user_login, name='login'),
    path('register/', logreg_views.register, name='register'),
    path('logout/', logreg_views.user_logout, name='logout'),
    path('welcome/', logreg_views.user_welcome, name='welcome'),
    path('reset/', include(reset_patterns)),
]


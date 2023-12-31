from django.urls import path
from . import views


urlpatterns = [
    path('crear_registro/', views.crear_registro, name='crear_registro'),
    path('lista_registros/', views.lista_registros, name='lista_registros'),
    path('send_email/', views.send_email_view, name='enviar_correo')
]

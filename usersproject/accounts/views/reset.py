from django.contrib.auth.views import PasswordResetView

class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset/password_reset_form.html'
    subject_template_name = 'reset/password_reset_subject.txt'
    html_email_template_name = 'reset/password_reset_email.html'
    content_type = 'text/html'
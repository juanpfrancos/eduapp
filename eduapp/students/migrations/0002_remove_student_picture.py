# Generated by Django 4.2.5 on 2023-12-29 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='picture',
        ),
    ]

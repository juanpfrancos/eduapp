# Generated by Django 4.2.5 on 2023-12-24 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_delete_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('observation', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]

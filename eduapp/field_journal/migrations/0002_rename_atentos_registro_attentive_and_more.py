# Generated by Django 4.2.5 on 2024-01-02 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('field_journal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='atentos',
            new_name='attentive',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='fecha',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='empleado',
            new_name='employee',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='actividades_interesantes',
            new_name='enough_time',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='influencias',
            new_name='influences',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='interrupciones',
            new_name='interesting_activities',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='material_agradable',
            new_name='interruptions',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='involucrados',
            new_name='involved',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='tiempo_suficiente',
            new_name='nice_materials',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='trabajo_fuera_aula',
            new_name='outside_working',
        ),
        migrations.RenameField(
            model_name='registro',
            old_name='situacion_relevante',
            new_name='relevant_situation',
        ),
    ]
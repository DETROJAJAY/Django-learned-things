# Generated by Django 4.1 on 2022-10-22 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_admdatetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='admdatetime',
        ),
    ]
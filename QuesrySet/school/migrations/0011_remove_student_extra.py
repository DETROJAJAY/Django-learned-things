# Generated by Django 4.1 on 2022-10-22 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_student_extra_student2_admdatetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='extra',
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudoperation', '0002_employee_works'),
    ]

    operations = [
        migrations.CreateModel(
            name='empl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]

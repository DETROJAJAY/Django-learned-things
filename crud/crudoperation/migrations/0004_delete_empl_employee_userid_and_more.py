# Generated by Django 4.1.2 on 2022-11-04 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudoperation', '0003_empl'),
    ]

    operations = [
        migrations.DeleteModel(
            name='empl',
        ),
        migrations.AddField(
            model_name='employee',
            name='userid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_works',
            name='workhours',
            field=models.IntegerField(),
        ),
    ]

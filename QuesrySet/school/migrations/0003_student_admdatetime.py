# Generated by Django 4.1 on 2022-10-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admdatetime',
            field=models.DateTimeField(default=6),
            preserve_default=False,
        ),
    ]
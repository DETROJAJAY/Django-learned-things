# Generated by Django 4.1 on 2022-10-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=30),
        ),
    ]
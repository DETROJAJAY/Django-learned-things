# Generated by Django 4.1 on 2022-10-11 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]

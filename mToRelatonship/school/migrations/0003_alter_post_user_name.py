# Generated by Django 4.1 on 2022-10-24 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school', '0002_alter_post_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

# Generated by Django 4.2 on 2023-04-09 11:16

from django.conf import settings
from django.db import migrations
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_alter_task_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

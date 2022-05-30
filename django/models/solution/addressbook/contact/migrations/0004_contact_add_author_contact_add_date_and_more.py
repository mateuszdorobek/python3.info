# Generated by Django 4.0.4 on 2022-05-30 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0003_alter_contact_lastname'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='add_author',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='add_author', to=settings.AUTH_USER_MODEL, verbose_name='Add Author'),
        ),
        migrations.AddField(
            model_name='contact',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Add Date'),
        ),
        migrations.AddField(
            model_name='contact',
            name='edit_autor',
            field=models.ForeignKey(blank=True, default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='edit_autor', to=settings.AUTH_USER_MODEL, verbose_name='Edit Author'),
        ),
        migrations.AddField(
            model_name='contact',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Edit Date'),
        ),
    ]

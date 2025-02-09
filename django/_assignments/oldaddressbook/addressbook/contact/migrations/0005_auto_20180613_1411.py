# Generated by Django 2.0.6 on 2018-06-13 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact', '0004_auto_20180613_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='reporter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Reporter'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), (None, 'Undisclosed')], default=None, max_length=30, null=True, verbose_name='Gender'),
        ),
    ]

# Generated by Django 2.0.6 on 2018-06-13 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20180613_1411'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='friends',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='contact.Contact', verbose_name='Friends'),
        ),
    ]

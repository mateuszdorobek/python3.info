# Generated by Django 2.0.6 on 2018-06-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_contact_friends'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Is deleted?'),
        ),
    ]

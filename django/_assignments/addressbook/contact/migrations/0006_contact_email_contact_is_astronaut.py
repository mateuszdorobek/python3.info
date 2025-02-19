# Generated by Django 4.0.4 on 2022-05-30 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_remove_contact_edit_autor_contact_edit_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='contact',
            name='is_astronaut',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Is Astronaut?'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contact', '0008_contact_group_contact_rank_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='group',
            field=models.ManyToManyField(blank=True, default=None, limit_choices_to={'group__name__startswith': 'contact'}, to='auth.group', verbose_name='Group'),
        ),
    ]

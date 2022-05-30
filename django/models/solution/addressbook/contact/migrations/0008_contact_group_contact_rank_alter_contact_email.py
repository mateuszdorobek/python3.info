# Generated by Django 4.0.4 on 2022-05-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contact', '0007_contact_height_contact_salary_contact_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='group',
            field=models.ManyToManyField(blank=True, default=None, limit_choices_to={'group__name__startswith': 'contact'}, null=True, to='auth.group', verbose_name='Group'),
        ),
        migrations.AddField(
            model_name='contact',
            name='rank',
            field=models.CharField(blank=True, choices=[('normal', 'Normal'), ('senior', 'Senior')], default='normal', max_length=15, null=True, verbose_name='Rank'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, default=None, max_length=254, null=True, unique=True, verbose_name='Email'),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-30 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0017_rename_contact_address_person_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='person',
            field=models.ForeignKey(default=None, null=None, on_delete=django.db.models.deletion.CASCADE, to='contact.person', verbose_name='Person'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='person',
            field=models.ForeignKey(default=None, null=None, on_delete=django.db.models.deletion.CASCADE, to='contact.person', verbose_name='Person'),
        ),
    ]

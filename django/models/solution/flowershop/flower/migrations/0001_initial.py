# Generated by Django 4.0.4 on 2022-05-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Iris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sepal_length', models.FloatField(blank=True, default=None, null=True, verbose_name='Sepal Length')),
                ('sepal_width', models.FloatField(blank=True, default=None, null=True, verbose_name='Sepal Width')),
                ('petal_length', models.FloatField(blank=True, default=None, null=True, verbose_name='Petal Length')),
                ('petal_width', models.FloatField(blank=True, default=None, null=True, verbose_name='Petal Width')),
                ('species', models.CharField(blank=True, default=None, max_length=20, null=True, verbose_name='Species')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='flower/', verbose_name='Image')),
            ],
        ),
    ]

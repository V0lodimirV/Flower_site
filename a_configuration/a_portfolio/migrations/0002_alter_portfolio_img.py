# Generated by Django 4.1.5 on 2023-01-04 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='img',
            field=models.ImageField(upload_to='portfolio', verbose_name='Изображения'),
        ),
    ]
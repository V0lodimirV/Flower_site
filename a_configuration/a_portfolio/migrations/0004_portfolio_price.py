# Generated by Django 4.1.5 on 2023-01-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_portfolio', '0003_alter_portfolio_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='price',
            field=models.CharField(default='price', max_length=20, verbose_name='цена'),
            preserve_default=False,
        ),
    ]

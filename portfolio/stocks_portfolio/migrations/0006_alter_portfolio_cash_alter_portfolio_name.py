# Generated by Django 4.2.4 on 2023-09-11 16:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks_portfolio', '0005_alter_portfolio_cash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='cash',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(1, message='Min amount is $1')], verbose_name='Initial cash'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Portfolio name'),
        ),
    ]

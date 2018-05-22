# Generated by Django 2.0.4 on 2018-05-19 21:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='ci',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message='Invalid format for CI', regex='^[0-9]{10}$')]),
        ),
    ]

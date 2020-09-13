# Generated by Django 3.1.1 on 2020-09-12 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200912_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='about',
            field=models.TextField(max_length=1000, null=True, validators=[django.core.validators.MinLengthValidator(50)]),
        ),
    ]
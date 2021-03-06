# Generated by Django 3.1.1 on 2020-09-12 11:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200911_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='heading',
            field=models.CharField(max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
        migrations.AlterField(
            model_name='blog',
            name='sub_heading',
            field=models.CharField(max_length=300, null=True, validators=[django.core.validators.MinLengthValidator(5), django.core.validators.MaxLengthValidator(15)]),
        ),
    ]

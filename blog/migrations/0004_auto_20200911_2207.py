# Generated by Django 3.1.1 on 2020-09-11 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200911_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='is_private',
            field=models.IntegerField(blank=True, choices=[(0, 'no'), (1, 'yes')], default=0, max_length=10),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-11 07:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210111_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default=datetime.date(2021, 1, 11), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(default=datetime.date(2021, 1, 11), max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(default=datetime.date(2021, 1, 11), max_length=50),
            preserve_default=False,
        ),
    ]

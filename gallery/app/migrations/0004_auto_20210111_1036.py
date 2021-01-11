# Generated by Django 3.1.5 on 2021-01-11 07:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='post_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image_name',
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_name',
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.RemoveField(
            model_name='image',
            name='category',
        ),
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.category'),
            preserve_default=False,
        ),
    ]

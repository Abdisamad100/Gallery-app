# Generated by Django 3.1.5 on 2021-01-10 16:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='app.category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location')),
            ],
        ),
    ]

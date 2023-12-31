# Generated by Django 4.2.4 on 2023-08-23 13:59

import Books.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('SureName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Slug', models.SlugField()),
                ('Year', models.IntegerField()),
                ('Rating', models.IntegerField(validators=[Books.models.validate_rating])),
                ('Watch_Count', models.IntegerField()),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.author')),
                ('Genre', models.ManyToManyField(to='Books.genre')),
            ],
        ),
    ]

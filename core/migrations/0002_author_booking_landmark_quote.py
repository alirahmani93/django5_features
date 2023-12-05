# Generated by Django 5.0 on 2023-12-05 08:12

import core.models
import django.contrib.postgres.fields
import django.contrib.postgres.fields.array
import django.contrib.postgres.fields.ranges
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('full_name', models.GeneratedField(db_persist=True, expression=core.models.ConcatOp('first_name', models.Value(' '), 'last_name'), output_field=models.TextField())),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('span', models.GeneratedField(db_persist=True, expression=core.models.DateRangeFunc('start', 'end'), output_field=django.contrib.postgres.fields.ranges.DateRangeField())),
            ],
        ),
        migrations.CreateModel(
            name='Landmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('reviews', django.contrib.postgres.fields.ArrayField(base_field=models.SmallIntegerField(), size=None)),
                ('count', models.GeneratedField(db_persist=True, expression=django.contrib.postgres.fields.array.ArrayLenTransform('reviews'), output_field=models.IntegerField())),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('text', models.TextField()),
                ('search', models.GeneratedField(db_persist=True, expression=django.contrib.postgres.search.SearchVector('text', config='english'), output_field=django.contrib.postgres.search.SearchVectorField())),
            ],
        ),
    ]

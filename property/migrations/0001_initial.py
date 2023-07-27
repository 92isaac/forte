# Generated by Django 4.2.3 on 2023-07-27 08:03

import cloudinary.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleImage',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, help_text='Model unique identifier', max_length=255, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation', verbose_name='date created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Date and time last modified', verbose_name='date modified')),
                ('multimage', cloudinary.models.CloudinaryField(default='https://via.placeholder.com/350x150', max_length=255, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, help_text='Model unique identifier', max_length=255, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation', verbose_name='date created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Date and time last modified', verbose_name='date modified')),
                ('title', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_rooms', models.PositiveIntegerField()),
                ('number_of_bath', models.PositiveIntegerField()),
                ('property_size', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'ordering': ('-created_date', 'title'),
            },
        ),
        migrations.CreateModel(
            name='ProPertyDescriptions',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, help_text='Model unique identifier', max_length=255, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation', verbose_name='date created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Date and time last modified', verbose_name='date modified')),
                ('description', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SingleImage',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, help_text='Model unique identifier', max_length=255, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation', verbose_name='date created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Date and time last modified', verbose_name='date modified')),
                ('image', cloudinary.models.CloudinaryField(default='https://via.placeholder.com/350x150', max_length=255, verbose_name='image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProPertyImages',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, help_text='Model unique identifier', max_length=255, primary_key=True, serialize=False, verbose_name='Unique ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='Date and time of creation', verbose_name='date created')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='Date and time last modified', verbose_name='date modified')),
                ('gallery', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_images', to='property.multipleimage')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

# Generated by Django 4.2.3 on 2023-07-27 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_gallery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='gallery',
            new_name='property_images',
        ),
    ]

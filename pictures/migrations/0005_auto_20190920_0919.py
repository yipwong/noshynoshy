# Generated by Django 2.1.12 on 2019-09-20 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0004_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='photo',
            new_name='image',
        ),
    ]

# Generated by Django 2.1.12 on 2019-09-17 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_delete_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='permalink',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]

# Generated by Django 3.2.23 on 2023-12-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='dni',
            field=models.CharField(max_length=9),
        ),
    ]

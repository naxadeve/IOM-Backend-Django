# Generated by Django 2.2.7 on 2019-12-16 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0058_gallery_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablefacility',
            name='name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

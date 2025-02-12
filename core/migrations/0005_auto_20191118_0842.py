# Generated by Django 2.2.7 on 2019-11-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191115_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openspace',
            name='capacity',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='openspace',
            name='total_area',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='openspace',
            name='usable_area',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=20, null=True),
        ),
    ]

# Generated by Django 2.2.7 on 2019-11-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20191126_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsdata',
            name='ans',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

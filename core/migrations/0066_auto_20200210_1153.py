# Generated by Django 2.2.6 on 2020-02-10 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0065_auto_20200119_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='token',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]

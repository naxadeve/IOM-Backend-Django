# Generated by Django 2.2.7 on 2019-12-12 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_auto_20191211_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 2.2.6 on 2020-04-01 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0012_whymapopenicon_icon_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutheader',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='aboutheader',
            name='description_nep',
            field=models.TextField(blank=True, null=True),
        ),
    ]

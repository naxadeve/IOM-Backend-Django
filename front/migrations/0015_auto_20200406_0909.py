# Generated by Django 2.2.6 on 2020-04-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0014_auto_20200401_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutheader',
            name='title',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='aboutheader',
            name='title_nep',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='openspacecriteria',
            name='title',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='openspacecriteria',
            name='title_nep',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='whymapopenspace',
            name='title',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='whymapopenspace',
            name='title_nep',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
    ]

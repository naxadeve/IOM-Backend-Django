# Generated by Django 2.2.7 on 2019-11-19 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0004_contact_openspaceapp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header',
            old_name='title',
            new_name='title1',
        ),
        migrations.RenameField(
            model_name='header',
            old_name='title_nep',
            new_name='title2',
        ),
        migrations.AddField(
            model_name='header',
            name='title3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='title_nep1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='title_nep2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='header',
            name='title_nep3',
            field=models.TextField(blank=True, null=True),
        ),
    ]

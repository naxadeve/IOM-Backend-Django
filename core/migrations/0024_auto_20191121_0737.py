# Generated by Django 2.2.7 on 2019-11-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20191121_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablefacility',
            name='operator_type',
            field=models.CharField(blank=True, choices=[('private', 'Private'), ('community', 'Community'), ('government', 'Government'), ('public', 'Public')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='availablefacility',
            name='type',
            field=models.CharField(blank=True, choices=[('health facility', 'Health Facility'), ('education facility', 'Education Facility'), ('security force', 'Security Force'), ('place of worship', 'Place Of Worship'), ('financial institution', 'Financial Institution')], max_length=30, null=True),
        ),
    ]

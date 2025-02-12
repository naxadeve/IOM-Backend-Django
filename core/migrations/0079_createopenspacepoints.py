# Generated by Django 2.2.6 on 2020-03-30 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_auto_20200324_0613'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateOpenSpacePoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('title_nep', models.CharField(blank=True, max_length=500, null=True)),
                ('steps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='create_open', to='core.CreateOpenSpace')),
            ],
        ),
    ]

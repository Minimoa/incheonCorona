# Generated by Django 3.0.4 on 2020-03-13 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200313_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='statistics',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
# Generated by Django 3.1 on 2020-11-19 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_App', '0013_auto_20201109_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='icon_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]

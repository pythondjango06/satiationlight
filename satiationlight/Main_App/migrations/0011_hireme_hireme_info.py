# Generated by Django 3.1 on 2020-11-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_App', '0010_hireme'),
    ]

    operations = [
        migrations.AddField(
            model_name='hireme',
            name='hireme_info',
            field=models.TextField(default=''),
        ),
    ]

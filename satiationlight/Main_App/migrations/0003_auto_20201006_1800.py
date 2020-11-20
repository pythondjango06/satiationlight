# Generated by Django 3.1 on 2020-10-06 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main_App', '0002_auto_20201006_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='category_name_in_smaill',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.CreateModel(
            name='Category_Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='Category/image')),
                ('category_name_in_smaill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main_App.category')),
            ],
            options={
                'verbose_name_plural': 'Category_Images',
            },
        ),
    ]

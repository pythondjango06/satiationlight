# Generated by Django 3.1 on 2020-11-09 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_App', '0011_hireme_hireme_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_image', models.ImageField(default='', upload_to='ConatctImage/image')),
            ],
            options={
                'verbose_name_plural': 'Conatct Image',
            },
        ),
        migrations.CreateModel(
            name='TestimonialImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_image', models.ImageField(default='', upload_to='TestimonialImage/image')),
            ],
            options={
                'verbose_name_plural': 'Testimonial Image',
            },
        ),
    ]

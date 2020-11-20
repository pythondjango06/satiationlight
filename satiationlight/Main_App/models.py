from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime,time
# Create your models here.

class Services(models.Model):

    icon_name = models.CharField(max_length=200, default="")
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default="")


    class Meta:
        verbose_name_plural = 'Services'


    def __str__(self):
        return self.name

class Category(models.Model):

    name = models.CharField(max_length=100, default="")
    category_name = models.CharField(max_length=100, default="")
    image = models.ImageField(upload_to='Category/image', default="")
    url = models.CharField(max_length=1000, default="")


    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name




# Create your models here.

class Blog(models.Model):

    author = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=2000)
    short_text = models.TextField()
    body_text = RichTextField(blank=True, null=True)
    date = models.DateTimeField(max_length=12)
    time = models.TimeField(max_length=12,default="00:00")
    image = models.ImageField(upload_to='blog/image')


    class Meta:
        verbose_name_plural = 'Blogs'


    def __str__(self):
        return self.author


class Testimonial(models.Model):

    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonial/image', default="")


    class Meta:
        verbose_name_plural = 'Testimonial'


    def __str__(self):
        return self.name



class Contact(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    message = models.TextField()


    class Meta:
        verbose_name_plural = 'Contact Us'


    def __str__(self):
        return self.name


class Logo(models.Model):

    logo1 = models.ImageField(upload_to='logo1/image', default="")
    logo2 = models.ImageField(upload_to='logo2/image', default="")


    class Meta:
        verbose_name_plural = 'Logo'


class Header(models.Model):

    header_image = models.ImageField(upload_to='header/image', default="")


    class Meta:
        verbose_name_plural = 'Header Image'


class Aboutus(models.Model):

    about_image = models.ImageField(upload_to='about/image', default="")
    about_info = models.TextField(default="")


    class Meta:
        verbose_name_plural = 'About Us '



class Hireme(models.Model):

    hireme_image = models.ImageField(upload_to='Hireme/image', default="")
    hireme_info = models.TextField(default="")


    class Meta:
        verbose_name_plural = 'Hireme Image'



class TestimonialImage(models.Model):

    testimonial_image = models.ImageField(upload_to='TestimonialImage/image', default="")


    class Meta:
        verbose_name_plural = 'Testimonial Image'


class ContactImage(models.Model):

    contact_image = models.ImageField(upload_to='ConatctImage/image', default="")


    class Meta:
        verbose_name_plural = 'Conatct Image'
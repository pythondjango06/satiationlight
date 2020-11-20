from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import Services,Blog, Testimonial, Contact, Category, Logo, Header, Aboutus, Hireme, TestimonialImage, ContactImage
import datetime
import random
# Create your views here.


def home(request):

    service = Services.objects.all()
    workcategory = Category.objects.all()
    blog = Blog.objects.all()
    testimonial = Testimonial.objects.all()
    work_category =  workcategory
    logo = Logo.objects.all()
    header_image = Header.objects.all()
    aboutus = Aboutus.objects.all()
    hireme = Hireme.objects.all()
    testimonial_image = TestimonialImage.objects.all()
    contact_image = ContactImage.objects.all()

    rand_num = random.randrange(1,2)

    CategoryList = []
    for cat in workcategory:
        if cat.category_name not in CategoryList and cat.category_name != "":
            CategoryList.append(cat.category_name)
    return render(request, 'home.html',{'service':service, 'testimonial_image':testimonial_image, 'contact_image':contact_image, 'hireme':hireme, 'aboutus':aboutus, 'header_image':header_image, 'rand_num':rand_num, 'CategoryList':CategoryList, 'Work_Category':work_category, 'blog':blog, 'testimonial':testimonial, 'logo':logo})


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        user = Contact(name=name, email=email, subject=subject, message=message)
        user.save()


        msg = "Your Message Successsfully Submitted"


    return render(request, 'home.html', {'msg':msg})

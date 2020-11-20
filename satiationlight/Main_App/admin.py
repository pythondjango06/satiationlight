from django.contrib import admin
from . models import Services, Blog, Testimonial, Contact, Category, Logo,Header, Aboutus, Hireme, TestimonialImage, ContactImage

# Register your models here.
class Dis_Services(admin.ModelAdmin):
    list_display = ('icon_name','name','description')
admin.site.register(Services, Dis_Services)



class Dis_Category(admin.ModelAdmin):
    list_display = ('category_name','image')

admin.site.register(Category, Dis_Category)




class Dis_Blog(admin.ModelAdmin):
    list_display = ('author','title','short_text','body_text','date','time','image')

admin.site.register(Blog, Dis_Blog)




class Dis_Testimonial(admin.ModelAdmin):
    list_display = ('name','occupation','feedback','image')

admin.site.register(Testimonial, Dis_Testimonial)




class Dis_Contact(admin.ModelAdmin):
    list_display = ('name','email','subject','message')

admin.site.register(Contact, Dis_Contact)



class Dis_Logo(admin.ModelAdmin):
    list_display = ('logo1','logo2')

admin.site.register(Logo, Dis_Logo)

class Dis_Header(admin.ModelAdmin):
    list_display = ('header_image',)

admin.site.register(Header, Dis_Header)


class Dis_Aboutus(admin.ModelAdmin):
    list_display = ('about_image','about_info',)

admin.site.register(Aboutus, Dis_Aboutus)


class Dis_Hireme(admin.ModelAdmin):
    list_display = ('hireme_image','hireme_info',)

admin.site.register(Hireme, Dis_Hireme)

class Dis_TestimonialImage(admin.ModelAdmin):
    list_display = ('testimonial_image',)

admin.site.register(TestimonialImage, Dis_TestimonialImage)


class Dis_ContactImage(admin.ModelAdmin):
    list_display = ('contact_image',)

admin.site.register(ContactImage, Dis_ContactImage)
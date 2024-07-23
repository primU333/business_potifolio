from django.db import models


class Business_Detail(models.Model):
    business_name = models.CharField(max_length=100, null=True, blank=True)
    business_phone = models.CharField(max_length=100, null=True, blank=True)
    business_whatsapp_no = models.CharField(max_length=100, null=True, blank=True)
    business_physical_address = models.CharField(max_length=200, null=True, blank=True)
    business_email = models.EmailField(null=True, blank=True)

    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)

    facebook_profile_url = models.URLField(blank=True)
    twitter_profile_url = models.URLField(blank=True)
    instagram_profile_url = models.URLField(blank=True)

    clients_map_image = models.ImageField(upload_to='business', blank=True, null=True
                                          )
    def __str__(self):
        return self.business_name
    
class Website_Info(models.Model):
    banner_image = models.ImageField(upload_to='info', null=True, blank=True)
    banner_heading_1 = models.CharField(max_length=200, null=True, blank=True)
    banner_subheading_heading_1 = models.CharField(max_length=200, null=True, blank=True)
    banner_description_1 = models.TextField(null=True, blank=True)
    banner_heading_2 = models.CharField(max_length=200, null=True, blank=True)
    banner_subheading_heading_2 = models.CharField(max_length=200, null=True, blank=True)
    banner_description_2 = models.TextField(null=True, blank=True)
    banner_heading_3 = models.CharField(max_length=200, null=True, blank=True)
    banner_subheading_heading_3 = models.CharField(max_length=200, null=True, blank=True)
    banner_description_3 = models.TextField(null=True, blank=True)

    about_us_heading = models.CharField(max_length=300, null=True, blank=True)
    products_count = models.IntegerField(default=1)
    clients_count = models.IntegerField(default=1)
    patners_count = models.IntegerField(default=1)
    users_count = models.IntegerField(default=1)
    about_us_sub_heading = models.CharField(max_length=300, null=True, blank=True)
    about_us_description = models.TextField(null=True, blank=True)
    about_us_image = models.ImageField(upload_to='info', default='default.jpg')

    services_heading = models.CharField(max_length=200, blank=True)
    services_sub_heading = models.CharField(max_length=200, blank=True)
    services_description = models.TextField(blank=True)

    who_we_are_sub_heading = models.CharField(max_length=200, blank=True)
    who_we_are_description = models.TextField(blank=True)
    who_we_are_image = models.ImageField(upload_to='info', default='default.jpg')

    def __str__(self) -> str:
        return 'Website Information'
    
class Objective(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Faq(models.Model):
    categories = (
        ('Websites','Websites'),
        ('Marketing','Marketing'),
        ('Branding','Branding'),
        ('E-Commerce','E-Commerce'),
        ('Support','Support'),
    )
    category = models.CharField(max_length=100, choices=categories)
    question = models.CharField(max_length=100)
    answer = models.TextField()

    def __str__(self):
        return self.question
    

class Team_Member(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='business', default='default.jpg')

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='info', default='default.jpg')
    product_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    testifier_name = models.CharField(max_length=100)
    testifier_category = models.CharField(max_length=100, blank=True)
    testifier_image = models.ImageField(upload_to='info', default='defsult.jpg')
    testimony = models.TextField()

    def __str__(self):
        return self.testifier_name
    

class Contact_Us_Message(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.subject
    
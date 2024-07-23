from django.contrib import admin
from .models import *

class BusinessAdmin(admin.ModelAdmin):
    search_fields = ['business_name']
admin.site.register(Business_Detail, BusinessAdmin)

class WebInfoAdmin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Website_Info, WebInfoAdmin)

class ObjAdmin(admin.ModelAdmin):
    search_fields = ['title']
admin.site.register(Objective, ObjAdmin)

class FaqAdmin(admin.ModelAdmin):
    list_display = ['question', 'category']
    search_fields = ['question', 'category']
admin.site.register(Faq, FaqAdmin)

class Team_MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    search_fields = ['name', 'position']
admin.site.register(Team_Member, Team_MemberAdmin)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title']
admin.site.register(Product, ProductAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    search_fields = ['testifier_name']
admin.site.register(Testimonial, TestimonialAdmin)

class ContMessAdmin(admin.ModelAdmin):
    search_fields = ['title']
admin.site.register(Contact_Us_Message, ContMessAdmin)



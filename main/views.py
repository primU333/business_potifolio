from django.shortcuts import render
from .models import *




def home(request):
    info = Website_Info.objects.all().last()
    buss = Business_Detail.objects.all().last()
    faqs = Faq.objects.all()
    products = Product.objects.all()
    tests = Testimonial.objects.all()
    team = Team_Member.objects.all()
    objs = Objective.objects.all()[:5]

    context = {
        'name' : buss.business_name,
        'business' : buss,
        'info' : info,
        'tests' : tests,
        'faqs' : faqs,
        'team' : team,
        'objs' : objs,
        'products' : products,
    }
    return render(request, 'main/index.html', context)
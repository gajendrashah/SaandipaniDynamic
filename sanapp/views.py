from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

import os
from django.shortcuts import render, get_object_or_404
from django.conf import settings

from django.contrib import messages
from .forms import ContactForm
from .models import Contact



# Create your views here.
from django.http import HttpResponse
from .models import Carousel, About, Service, Testimonial, TopDestination, FAQ, StudyCountry, Country, PopularCourse, Advertisement, QuoteForm, ExpertTeam, Footer


def indexabc(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    carousel = Carousel.objects.all()
    about = About.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    top_destinations = TopDestination.objects.all()
    faqs = FAQ.objects.all()
    countries = Country.objects.all() 
    expert_team = ExpertTeam.objects.all()
    ads = Advertisement.objects.filter(is_active=True)  
    fdetails = Footer.objects.all()
    country = Country.objects.all()
    return render(request, "sanapp/index.html", {"countries": countries,"carousel": carousel, "about": about, "services": services, "testimonials": testimonials, "top_destinations": top_destinations, "faqs": faqs, "ads": ads, "expert_team": expert_team, "fdetails": fdetails, "country": country})




def country(request, country_name):
    countries = Country.objects.all()
    study_country = StudyCountry.objects.filter(country__name__iexact=country_name)
    popular_courses = PopularCourse.objects.all()
    faqs = FAQ.objects.all()
    fdetails = Footer.objects.all()
    return render(request, f"sanapp/study/{country_name}.html", {"study_country": study_country, "countries": countries, "popular_courses": popular_courses, "faqs": faqs, "fdetails": fdetails})
    
def aboutPage(request):
    countries = Country.objects.all()
    about = About.objects.all()
    services = Service.objects.all()
    expert_team = ExpertTeam.objects.all()
    fdetails = Footer.objects.all()
    return render(request, "sanapp/about.html", {"countries": countries, "about": about, "services": services, "expert_team": expert_team, "fdetails": fdetails})



def servicePage(request):
    services = Service.objects.all()
    countries = Country.objects.all()       
    testimonials = Testimonial.objects.all() 
    fdetails = Footer.objects.all()
    return render(request, "sanapp/service.html", {"services": services, "testimonials": testimonials, "countries": countries, "fdetails": fdetails})

from django.http import JsonResponse

def contactPage(request):
    countries = Country.objects.all() 
    fdetails = Footer.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'message': 'Please correct the errors below.', 'errors': errors})
    else:
        form = ContactForm()
    return render(request, "sanapp/contact.html", {"countries": countries, "fdetails": fdetails, "form": form})


def blogPage(request):
    countries = Country.objects.all() 
    fdetails = Footer.objects.all()
    return render(request, "sanapp/work-in-japan.html", {"countries": countries, "fdetails": fdetails})

def get_quote(request):
    ads = Advertisement.objects.filter(is_active=True)
    if request.method == "POST":
        form = QuoteForm(request.POST)
        if form.is_valid():

            # Process the form (e.g., save to DB, send email)
            return JsonResponse({"success": True, "message": "Your quote request has been submitted!"})
        else:
            return JsonResponse({"success": False, "errors": form.errors})

    form = QuoteForm()
    return render(request, "sanapp/getquote.html", {"form": form})

def ads_view(request):
    ads = Advertisement.objects.filter(is_active=True)
    return render(request, 'ad.html', {'ads': ads})


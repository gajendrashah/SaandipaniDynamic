from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("study/<str:country_name>/", views.country, name="country"),
    path("about/", views.aboutPage, name="about"),
    path("service/", views.servicePage, name="service"),
    path("contact/", views.contactPage, name="contact"),
    path("work-in-japan/", views.blogPage, name="work-in-japan"),
    path("quote/", views.get_quote, name="quote"),
    path('ads/', views.ads_view, name='ads'),
]
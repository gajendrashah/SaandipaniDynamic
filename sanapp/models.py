from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from django import forms
from django.contrib.auth.models import User
    
class Carousel(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    quote = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='services/')
    def __str__(self):
        return self.title
    
class About(models.Model):
    title = models.CharField(max_length=200)
    vision = RichTextField()
    mission = RichTextField()
    description = RichTextField()
    image = models.ImageField(upload_to='about/')
    def __str__(self):
        return self.title
    
class TopDestination(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='top_destination/')
    def __str__(self):
        return self.title
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='testimonial/')
    def __str__(self):
        return self.name
    
class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = HTMLField()
    def __str__(self):
        return self.question
    
class Country(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='country/')
    def __str__(self):
        return self.name

class StudyCountry(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    why_study = RichTextField()
    education_system = RichTextField()
    visa_process = RichTextField()
    work_permit = RichTextField()
    work_visa = RichTextField()
    choose_university = RichTextField()
    expenses = RichTextField()
    image = models.ImageField(upload_to='study_country/')
    def __str__(self):
        return self.title

class PopularCourse(models.Model):
    country = models.ForeignKey(StudyCountry, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='popular_course/')
    def __str__(self):
        return self.title


class QuoteForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    def __str__(self):
        return self.name
    
class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='ads/')
    link = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class ExpertTeam(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to='expert_team/')
    def __str__(self):
        return self.name
        

class Footer(models.Model):
    footerLogo = models.ImageField(upload_to='footer_content/')
    footerdes = RichTextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="social_links")
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    newdes = RichTextField()
    phoneno = models.CharField(max_length=200)
    mailid = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    project = models.CharField(max_length=200, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
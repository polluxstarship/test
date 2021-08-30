from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    poll = {
        'see': 'this is a test',
        'gee': 123,
        'qee': [123, 234, 345, 'gg']
    }
    return render(request, "about.html", poll)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def base_view(request, *args, **kwargs):
    return render(request, "base.html", {})
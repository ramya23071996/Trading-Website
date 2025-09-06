from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Trade


def home(request):
    return render(request, 'trade/home.html')

def about_us(request):
    return render(request, 'trade/about_us.html')

def blogs(request):
    return render(request, 'trade/blogs.html')

def become_partner(request):
    return render(request, 'trade/become_partner.html')

def login_page(request):
    return render(request, 'trade/login_page.html')

def register(request):
    return render(request, 'trade/register.html')
# apps/pages/views.py
from django.shortcuts import render

def landing_view(request):
    return render(request, 'landing.html')  # looks in nursTrac/templates/landing.html

def login_view(request):
    return render(request, 'login.html')

def log_hours_view(request):
    return render(request, 'log_hours.html')


# Create your views here.

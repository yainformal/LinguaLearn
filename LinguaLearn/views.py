"""
Система управления визуализацией 
"""
import datetime
from .models import CustomUser
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def user_auth_view(request):
    return render(request, "auth.html")


def register(request):
    return render(request, "register.html")


def customer_registered(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date = request.POST.get('birth_date')
        format_birth_date = datetime.datetime.strptime(birth_date, '%d.%m.%Y').date()
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = CustomUser(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            birth_date=format_birth_date
        )
        customer.save()
        return render(request, "success.html")
    else:
        return render(request, 'error.html')
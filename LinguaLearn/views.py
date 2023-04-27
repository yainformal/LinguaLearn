"""
Система управления визуализацией 
"""
import datetime

from django.db import IntegrityError

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
from django.contrib.auth.hashers import make_password


def index(request):
    return render(request, "index.html")


def user_auth_view(request):
    return render(request, "auth.html")


def register(request):
    return render(request, "register.html")


def customer_registered(request):
    if request.method == 'POST':
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            birth_date = request.POST.get('birth_date')
            format_birth_date = datetime.datetime.strptime(birth_date, '%d.%m.%Y').date()
            email = request.POST.get('email')
            password = request.POST.get('password')
            hashed_password = make_password(password)

            customer = CustomUser(
                email=email,
                password=hashed_password,
                first_name=first_name,
                last_name=last_name,
                birth_date=format_birth_date
            )
            customer.save()

            customer = CustomUser.objects.get(email=email)
            context = {
                'CustomUser': customer
            }

            return render(request, "success.html", context)
        except IntegrityError as e:
            error_message = 'Ошибка: пользователь с таким e-mail существует'
            return render(request, 'register.html', {'error_message': error_message})
    else:
        return render(request, 'error.html')


def det_customer_pofile(request):
    pass

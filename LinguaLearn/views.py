"""
Система управления визуализацией 
"""
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm



def index(request):
    return render(request, "index.html")


def user_auth_view(request):
    return render(request, "auth.html")


def register(request):
    return render(request, "register.html")



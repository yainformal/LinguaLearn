"""
Система управления визуализацией 
"""
from django.shortcuts import render, redirect
from django.core.cache import cache


def index(request):
    return render(request, "index.html")


def user_auth_view(request):
    return render(request, "auth.html")

"""
Система управления визуализацией 
"""
from django.shortcuts import render, redirect
from django.core.cache import cache


def index(request):
    return render(request, "index_b.html")


def user_auth_view(request):
    return render(request, "auth_b.html")

def authentication(request):
    if request.method == 'POST':
        # Получаем значения из формы
        username = request.POST.get('username')
        password = request.POST.get('password')
        """
        # Выполняем проверку данных
        if username and password:
            #TODO: реализовать первую базу данных, для проверки логина и пароля
            #Если данные прошли проверку, выполняем необходимые действия
            return redirect('')  # перенаправление на домашнюю страницу или другую страницу
         """
        # ... остальной код вашего представления ...
    return index(request)
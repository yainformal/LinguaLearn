"""
Система управления визуализацией 
"""
import datetime
from django.utils import timezone

from django.contrib import messages
from django.db import IntegrityError

from .models import CustomUser, Dictionary
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


def add_word(request):
    return render(request, "add_word.html")


def adding_word(request):
    if request.method == 'POST':
        try:
            word = request.POST.get('input_word')
            translate = request.POST.get('input_translate')

            # создаем новый объект Dictionary с полученными данными и сохраняем его в базе данных
            dictionary = Dictionary(
                word=word,
                translate=translate
            )
            dictionary.save()
            
            # выводим сообщение об успехе и перенаправляем пользователя на страницу с формой добавления слова
            messages.success(request, 'Слово успешно добавлено в словарь!')
            return dictionary_fill(request)

        except IntegrityError as e:
            error_message = 'Ошибка: слово уже есть в словаре'
            context = {
                'error_message': error_message,
                'word': word,
                'translate': translate
            }
            return render(request, 'add_word.html', context)
    else:
        # если метод запроса не POST, то возвращаем страницу с ошибкой
        return render(request, 'error.html')


def dictionary_fill(request):
    words = Dictionary.objects.all()
    context = {'words': words}
    return render(request, 'dictionary.html', context)


def edit_word(request, note_id):
    word = get_object_or_404(Dictionary, note_id=note_id)
    if request.method == 'POST':
        try:
            word.word = request.POST['word']
            word.translate = request.POST['translate']
            word.save()
            messages.success(request, 'Слово успешно изменено')
            return dictionary_fill(request)

        except IntegrityError as e:
            error_message = 'Ошибка: слово уже есть в словаре'
            context = {'word': word,'error_message': error_message}
            return render(request, 'edit_word.html',context)
    else:
        return render(request, 'edit_word.html', {'word': word})


def delete_word(request, note_id):
    word = get_object_or_404(Dictionary, note_id=note_id)
    word.delete()
    messages.success(request, 'Слово успешно удалено')
    return dictionary_fill(request)

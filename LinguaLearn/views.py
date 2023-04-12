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


def index(request):
    return render(request, "index.html")


def user_auth_view(request):
    return render(request, "auth.html")

def authentication(request):
    if request.method == 'POST':
        # Получаем значения из формы
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password) # метод аутентификации

        if user is not None:
            # Если пользователь найден, проводим вход в систему
            login(request, user)
            return HttpResponse('Вход в систему успешно выполнен.')
        else:
            return HttpResponse('Ошибка: неверный логин или пароль.')
    else:
        return render(request, 'auth.html')

    return index(request)   #TODO: необходимо проработать маршрут для авторизованного пользователя



@login_required
def upload_avatar(request):
    """
    Представление для загрузки аватара пользователя.
    """
    if request.method == 'POST':
        image = request.FILES['avatar']
        user = get_user_model().objects.get(username=request.user.username)
        # Удаляем старый аватар пользователя, если он существует
        if user.avatar:
            default_storage.delete(user.avatar.path)
        # Загружаем новый аватар
        user.avatar = image
        user.save()
        return redirect('profile')  #TODO создать страницу перенаправляем на страницу профиля пользователя
    return render(request, 'upload_avatar.html')  #TODO:создать  страницу отображаем форму загрузки аватара

@login_required
def delete_avatar(request):
    """
    Представление для удаления аватара пользователя.
    """
    if request.method == 'POST':
        user = get_user_model().objects.get(username=request.user.username)
        # Удаляем аватар пользователя, если он существует
        if user.avatar:
            default_storage.delete(user.avatar.path)
            user.avatar = None
            user.save()
        return redirect('profile')  #TODO: перенаправляем на страницу профиля пользователя (необходимо реализовать)
    return render(request, 'delete_avatar.html')  # отображаем форму удаления аватара

@login_required
def get_full_name(request):
    """
    Представление для получения полного имени пользователя (имени и фамилии).
    """
    user = get_user_model().objects.get(username=request.user.username)
    full_name = user.get_full_name()
    return render(request, 'full_name.html', {'full_name': full_name})  # отображаем полное имя пользователя






"""
Система управления визуализацией 
"""
from django.shortcuts import render, redirect
from django.core.cache import cache
from django.shortcuts import render
from django.core.files.storage import default_storage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


def index(request):
    return render(request, "index.html")


def user_auth_view(request):
    return render(request, "auth.html")

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
        return redirect('profile')  # перенаправляем на страницу профиля пользователя
    return render(request, 'upload_avatar.html')  # отображаем форму загрузки аватара

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
        return redirect('profile')  # перенаправляем на страницу профиля пользователя
    return render(request, 'delete_avatar.html')  # отображаем форму удаления аватара

@login_required
def get_full_name(request):
    """
    Представление для получения полного имени пользователя (имени и фамилии).
    """
    user = get_user_model().objects.get(username=request.user.username)
    full_name = user.get_full_name()
    return render(request, 'full_name.html', {'full_name': full_name})  # отображаем полное имя пользователя






"""
Файл содержащий описание моделей приложения
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """
    Модель авторизованного пользователя
    """
    # Поля для авторизационных данных
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # Дополнительные поля для профиля пользователя
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)




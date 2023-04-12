"""
Файл содержащий описание моделей приложения
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(models.Model):
    """
    Модель авторизованного пользователя
    """
    # Поля для авторизационных данных
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # Дополнительные поля для профиля пользователя
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

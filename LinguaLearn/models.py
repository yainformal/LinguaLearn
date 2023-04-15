"""
Файл содержащий описание моделей приложения
"""
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(models.Model):
    """
    Модель авторизованного пользователя
    """
    # Поля для авторизации
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    # Дополнительные поля для профиля пользователя
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    avatar = models.FileField(upload_to='avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'lingualearn_customer'


class Dictionary(models.Model):
    """
    Модель словаря пользователя
    """
    note_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=32, db_column='word')
    translate = models.CharField(max_length=256, db_column='translate')
    add_date = models.DateTimeField(db_column='add_dttm')
    customer_added = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=-1)
    card_img = models.FileField(upload_to='cards/',blank=True, null=True)
    speech = models.FileField(upload_to='speech/', blank=True, null=True)

    class Meta:
        db_table = 'lingualearn_dictionary'


class CustomerSession(models.Model):
    session_id = models.CharField(max_length=64, unique=True)
    customer_id = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=-1)
    start_dttm = models.DateTimeField(null=False)
    end_dttm = models.DateTimeField()

    class Meta:
        db_table = 'lingualearn_customer_session'
"""
Файл содержащий описание моделей приложения
"""

from django.db import models


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

    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    class Meta:
        db_table = 'customer'


class Dictionary(models.Model):
    """
    Модель словаря пользователя
    """
    note_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=32, db_column='word')
    translate = models.CharField(max_length=256, db_column='translate')
    add_date = models.DateTimeField(db_column='add_dttm')
    customer_added = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=-1)

    class Meta:
        db_table = 'dictionary'

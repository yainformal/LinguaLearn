"""
Конфигурационный файл, для выполнения функции при запуске приложения
"""

from django.apps import AppConfig
from django.core.management import call_command

class MyAppConfig(AppConfig):
    name = 'LinguaLearn'

    def ready(self):
        # команда для запуска миграции моделей в базу данных при запуске приложения
        call_command('migrate')

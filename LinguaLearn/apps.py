"""
Конфигурационный файл, для выполнения функции при запуске приложения
"""

from django.apps import AppConfig
from django.core.management import call_command
from .initializers import init_app_components

class MyAppConfig(AppConfig):
    name = 'LinguaLearn'
    global_components = None

    def ready(self):
        # команда для запуска миграции моделей в базу данных при запуске приложения
        call_command('migrate')
        MyAppConfig.global_components = init_app_components()
        

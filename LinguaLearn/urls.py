"""
URL configuration for LinguaLearn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path

from utils import feature
from . import views, api
from .views import customer_registered, adding_word
from django.urls import include

urlpatterns = {
    # path("admin/", admin.site.urls),
    path('', views.index),  # если нет пути, то главная страница
    path('index/', views.index),
    path('user_auth/', views.user_auth_view),  # ссылка на страницу авторизации
    # path('authentication/', views.authentication)
    path('register/', views.register),
    path('register/customer_registered/', customer_registered, name='customer_registered'),
    path('add_word/', views.add_word),
    path('adding_word/', adding_word, name='add_word'),
    path('dictionary_fill/', views.dictionary_fill, name='dictionary'),
    path('edit_word/<int:note_id>/', views.edit_word, name='edit_word'),
    path('delete_word/<int:note_id>/', views.delete_word, name='delete_word'),
    path('validate_password/', views.validate_password, name='validate_password'),
    path('log_out/<int:customer_id>/', views.log_out, name='log_out'),
    path('bot_page/', views.get_chat_bot, name='chat_bot'),
    path('api/response-lookup/', api.ResponseLookupView.as_view(), name='response-lookup'),
    path('api/generative-response/',api.GenerateResponseLookupView.as_view(), name='generative-response')
}

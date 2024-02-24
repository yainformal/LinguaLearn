"""
Файл содержащий описание моделей приложения
"""
import pickle
from django.db import models
from datetime import datetime



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
    registration_date = models.DateTimeField(null=True, default=datetime.now())

    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'lingualearn_customer'


class Dictionary(models.Model):
    """
    Модель словаря пользователя
    """
    note_id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=32, db_column='word', unique=True)
    translate = models.CharField(max_length=256, db_column='translate')
    add_date = models.DateTimeField(db_column='add_dttm', default=datetime.now(), null=True)

    class Meta:
        db_table = 'lingualearn_dictionary'


class CustomerSession(models.Model):
    session_id = models.CharField(max_length=64, unique=True)
    customer = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=-1)
    start_dttm = models.DateTimeField(null=False)
    end_dttm = models.DateTimeField(default='5999-12-31 00:00:00')

    class Meta:
        db_table = 'lingualearn_customer_session'


class QAHouset(models.Model):
    questions = models.TextField(null=True, blank=True)
    answers = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'lingualearn_QA_House'

#TODO: модель данных реализована,однако проект реализован на локальных данны без обращения к базе данных
class QuestionEmbedding(models.Model):
    qa_house = models.OneToOneField(QAHouset, on_delete=models.CASCADE, related_name='question_embedding')
    embedding = models.BinaryField()

    def set_embedding(self, numpy_array):
        self.embedding = pickle.dumps(numpy_array)

    def get_embedding(self):
        return pickle.loads(self.embedding)

    class Meta:
        db_table = 'lingualearn_QE_House'


class AnswerEmbedding(models.Model):
    qa_house = models.OneToOneField(QAHouset, on_delete=models.CASCADE, related_name='answer_embedding')
    embedding = models.BinaryField()

    def set_embedding(self, numpy_array):
        self.embedding = pickle.dumps(numpy_array)

    def get_embedding(self):
        return pickle.loads(self.embedding)

    class Meta:
        db_table = 'lingualearn_AE_House'





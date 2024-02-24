"""
Настройки конфигурации и ключи проекта
"""

import torch
import numpy as np
import random
import logging
from transformers import BertTokenizer

secret_django_key = "django-insecure-7o4)osm4x4t1-i(+1_x5q-2k=zq4*+_zf4_t(n2o&g6mb9l6ch"
DEBUG_PARAM = True


class Config:
    def __init__(self):
        self.mnist_path = None
        self.batch_size = 16
        self.lr = 3e-5  # из оригинальной статьи
        self.num_workers = 3
        self.num_epochs = 3
        self.MAX_LENGTH = 256
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.seed = 10  # Зерно для генерации случайных чисел для модуля random
        self.deterministic = True  # Включает флаг deterministic для бэкэнда cudnn в torch. Гарантирует воспроизводимость резульатов на GPU
        self.benchmark = False  # тключает автоматическую настройку библиотеки cudnn для оптимизации производительности. Гарантирует воспроизводимость резульатов на GPU

        self.tokenizer_class = BertTokenizer
        self.pretrained_model_name = 'bert-base-uncased'  # колонизатор
        self.Sbert_path = 'moduls/trained_models/sbert_softmax_lr_3e-5_16_256_2v1'
        self.CrossEncoder_path = 'moduls/trained_models/CrossEncoderBertlr_3e-5_16_256_v2'
        self.questions_matrix_path = 'moduls/matrix/matrix_Sbert_learning(questions).npy'
        self.answers_matrix_path = 'moduls/matrix/matrix_Sbert_learning(answers).npy'
        self.data_path = 'moduls/Data'

        self.logger = logging.getLogger('LinguaLearn')

    def apply_seed(self):
        """Применяет генерацию случайных чисел и настройки CuDNN."""
        random.seed(self.seed)
        np.random.seed(self.seed)  # использование зерна для np
        torch.manual_seed(self.seed)  # использование зерна для torch
        torch.cuda.manual_seed_all(self.seed)  # для всех доступных GPU

        # Настройки для обеспечения детерминированного поведения
        torch.backends.cudnn.deterministic = self.deterministic
        torch.backends.cudnn.benchmark = self.benchmark

    def init_tokenizer(self):
        """Инициализирует токенизатор с указанной предобученной моделью."""
        self.tokenizer = self.tokenizer_class.from_pretrained(self.pretrained_model_name)
        return self.tokenizer

    def print_config(self):
        """Печатает текущие настройки конфигурации."""
        print("Текущая конфигурация:")
        for attribute, value in self.__dict__.items():
            print(f"{attribute}: {value}")


config = Config()

import torch
from conf import config
from transformers import BertModel, BertTokenizer

from utils.feature import mean_pool


class Sbert(torch.nn.Module):
    def __init__(self, model_path=None, model_name='bert-base-uncased', max_length=config.MAX_LENGTH):
        super(Sbert, self).__init__()
        self.device = config.device
        self.max_length = max_length
        print(model_path)
        config.logger.info(model_path)
        # Проверка на наличие предобученной модели для загрузки
        if model_path:
            config.logger.info(f"Загрузка модели Bi Encoder  из {model_path}")
            self.bert_model = BertModel.from_pretrained(model_path)
            self.bert_tokenizer = BertTokenizer.from_pretrained(model_path)
        else:
            #print(f"Загрузка модели {model_name}")
            config.logger.info(f"Загрузка модели Bi Encoder {model_name}")
            self.bert_model = BertModel.from_pretrained(model_name)
            self.bert_tokenizer = BertTokenizer.from_pretrained(model_name)

        self.linear = torch.nn.Linear(self.bert_model.config.hidden_size * 3, 3)
        self.to(self.device)

    def forward(self, batch: dict) -> torch.tensor:

        answers_input_ids = batch["answers_input_ids"]
        answers_attention_mask = batch["answers_attention_mask"]
        questions_input_ids = batch["questions_input_ids"]
        questions_attention_mask = batch["questions_attention_mask"]

        out_answers = self.bert_model(answers_input_ids, attention_mask=answers_attention_mask)
        out_questions = self.bert_model(questions_input_ids, attention_mask=questions_attention_mask)

        answers_embeds = out_answers.last_hidden_state
        questions_embeds = out_questions.last_hidden_state

        # Применяем mean_pool для пулинга эмбеддингов
        pooled_answers_embeds = mean_pool(answers_embeds, answers_attention_mask)
        pooled_questions_embeds = mean_pool(questions_embeds, questions_attention_mask)

        # Конкатенация эмбеддингов и их разности
        embeds = torch.cat([
            pooled_answers_embeds, pooled_questions_embeds,
            torch.abs(pooled_answers_embeds - pooled_questions_embeds)
        ], dim=-1)

        return self.linear(embeds)


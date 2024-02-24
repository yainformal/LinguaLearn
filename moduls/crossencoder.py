import torch

from conf import config
from transformers import BertModel, BertTokenizer


class CrossEncoderBert(torch.nn.Module):
    def __init__(self, model_path=None, model_name='bert-base-uncased', max_length: int = config.MAX_LENGTH):
        super().__init__()
        self.max_length = max_length
        self.device = config.device

        if model_path:
            # print(f"Загрузка предобученной модели из {model_path}")
            config.logger.info(f"Загрузка модели CrossEncoder из {model_path}")
            self.bert_model = BertModel.from_pretrained(model_path)
            self.bert_tokenizer = BertTokenizer.from_pretrained(model_path)

        else:
            # print(f"Загрузка  модели  {model_name}")
            config.logger.info(f"Загрузка модели CrossEncoder {model_name}")
            self.bert_model = BertModel.from_pretrained(model_name)
            self.bert_tokenizer = BertTokenizer.from_pretrained(model_name)

        self.linear = torch.nn.Linear(self.bert_model.config.hidden_size, 1)

        self.to(self.device)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert_model(input_ids=input_ids, attention_mask=attention_mask)
        pooled_output = outputs.last_hidden_state[:, 0]  # Use the CLS token's output
        return self.linear(pooled_output)


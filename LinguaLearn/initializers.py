from moduls.crossencoder import CrossEncoderBert
from moduls.sbert import Sbert
from conf import config

import numpy as np
from datasets import load_from_disk
from transformers import BertTokenizer, BertModel


def init_app_components():
    global model, CrossEncoder, tokenizer, answers_Sbert_embeddings, questions_Sbert_embeddings, data, answers, answer_params, questions_params
    model = Sbert(config.Sbert_path)
    CrossEncoder = CrossEncoderBert(config.CrossEncoder_path)
    tokenizer = config.init_tokenizer()
    answers_Sbert_embeddings = np.load(config.answers_matrix_path)
    questions_Sbert_embeddings = np.load(config.questions_matrix_path)
    data = load_from_disk(config.data_path)
    answers = data["answers"]
    answer_params = [
        answers_Sbert_embeddings,
        answers,  # answers list
        model.bert_tokenizer,  # tokenizer
        model.bert_model,  # model
        config.device,
        5  # top relevants answer
    ]
    questions_params = [
        questions_Sbert_embeddings,
        answers,  # answers list
        model.bert_tokenizer,  # tokenizer
        model.bert_model,  # model
        # key, # questions \ answers
        config.device,
        5
    ]
    components = {
        "model": model,
        "CrossEncoder": CrossEncoder,
        "tokenizer": tokenizer,
        "answers_Sbert_embeddings": answers_Sbert_embeddings,
        "questions_Sbert_embeddings": questions_Sbert_embeddings,
        "data": data,
        "answers": answers,
        "answer_params": answer_params,
        "questions_params": questions_params
    }

    return components


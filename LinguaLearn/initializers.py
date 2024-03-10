from moduls.crossencoder import CrossEncoderBert
from moduls.sbert import Sbert
from transformers import T5ForConditionalGeneration, AutoTokenizer
from conf import config

import numpy as np
from datasets import load_from_disk


def init_app_generative_components():
    global model, tokenizer, generation_options
    model = T5ForConditionalGeneration.from_pretrained(config.T5_path).to(config.device)
    tokenizer = config.init_tokenizer()
    generation_options = {
        'do_sample': True,
        'max_new_tokens': 20,
        'temperature': 0.9,
        'repetition_penalty': 1.5,
        'num_beams': 1,
        'top_k': 50,
        'top_p': 0.85,
        'max_length': config.MAX_LENGTH
    }

    components = {
        "model": model,
        "tokenizer": tokenizer,
        "generation_options": generation_options
    }

    return components


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

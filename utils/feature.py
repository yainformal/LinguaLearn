import asyncio
import numpy as np
import time
from transformers import BertModel, BertTokenizer
import torch
from conf import config
from moduls.crossencoder import CrossEncoderBert
from scipy.spatial.distance import cdist
from datasets import load_from_disk

#answers_Sbert_embeddings = np.load(config.answers_matrix_path)
#questions_Sbert_embeddings = np.load(config.questions_matrix_path)

#data = load_from_disk(config.data_path)
#answers = data["answers"]



def mean_pool(token_embeds: torch.tensor, attention_mask: torch.tensor) -> torch.tensor:
    in_mask = attention_mask.unsqueeze(-1).expand(token_embeds.size()).float()
    pool = torch.sum(token_embeds * in_mask, 1) / torch.clamp(in_mask.sum(1), min=1e-9)
    return pool


def encode(input_texts: list[str], tokenizer, model, device=config.device
           ) -> torch.tensor:
    model.eval()
    tokenized_texts = tokenizer(input_texts, max_length=config.MAX_LENGTH,
                                padding='max_length', truncation=True, return_tensors="pt")
    token_embeds = model(tokenized_texts["input_ids"].to(device),
                         tokenized_texts["attention_mask"].to(device)).last_hidden_state
    pooled_embeds = mean_pool(token_embeds, tokenized_texts["attention_mask"].to(device))
    return pooled_embeds


async def generate_embeddings(dataset, model, tokenizer, device, key='answers'):
    model.eval()
    embeddings = []
    with torch.no_grad():
        for i in range(len(dataset)):
            item = dataset[i]
            item_key = str(item[key])
            inputs = tokenizer(item_key, return_tensors="pt", padding=True, truncation=True,
                               max_length=config.MAX_LENGTH)
            inputs = {k: v.to(device) for k, v in inputs.items()}
            outputs = model(**inputs)
            embeddings.append(outputs.pooler_output.squeeze().cpu().numpy())

    return embeddings


async def find_top_k_relevant_answers_with_indices(question_embeddings, answers, tokenizer, model, device, k, question,
                                             key='answers'):
    # Генерация эмбеддинга для заданного вопроса
    request_embedding = await generate_embeddings([{key: question}], model, tokenizer, device, key)
    request_embedding = request_embedding[0].reshape(1, -1)
    # Вычисление косинусного сходства между эмбеддингом вопроса и эмбеддингами ответов
    similarities = 1 - cdist(request_embedding, question_embeddings, 'cosine').flatten()

    # Идентификация топ-K релевантных ответов
    top_k_indices = np.argsort(similarities)[-k:][::-1]
    top_k_answers_with_indices = [(answers[i], similarities[i]) for i in top_k_indices]

    return top_k_answers_with_indices


def get_ranked_docs(
        tokenizer: BertTokenizer, finetuned_ce: CrossEncoderBert,
        query: str, corpus: list[str]
) -> None:
    queries = [query] * len(corpus)
    tokenized_texts = tokenizer(
        queries, corpus, max_length=config.MAX_LENGTH, padding=True, truncation=True, return_tensors="pt"
    ).to(config.device)

    # Finetuned CrossEncoder model scoring
    with torch.no_grad():
        ce_scores = finetuned_ce(tokenized_texts['input_ids'], tokenized_texts['attention_mask']).squeeze(-1)
        ce_scores = torch.sigmoid(ce_scores)  # Apply sigmoid if needed

    # print(f"Query - {query} [Finetuned Cross-Encoder]\n---")
    scores = ce_scores.cpu().numpy()
    scores_ix = np.argsort(scores)[::-1]

    ranked_docs = [(corpus[ix], scores[ix]) for ix in scores_ix]  # Создаем список кортежей (документ, скор)

    top_doc = ranked_docs[0][0] if ranked_docs else (None, None)   #TODO: Получаем ответ -- костыль из теста. Надо переделать

    return top_doc


async def response_lookup(new_question, questions_params, answer_params, tokenizer, CrossEncoder):
    start_time = time.time()

    top_k_questions_with_indices = await find_top_k_relevant_answers_with_indices(*questions_params, new_question, key='questions')
    config.logger.info(f"find_top_k_relevant_answers_with_indices (questions): {time.time() - start_time:.2f} сек.")
    start_time = time.time()
    top_k_answers_with_indices = await find_top_k_relevant_answers_with_indices(*answer_params, new_question, key="answer")
    config.logger.info(f"find_top_k_relevant_answers_with_indices (answers): {time.time() - start_time:.2f} сек.")
    start_time = time.time()
    corpus = [item[0] for item in top_k_answers_with_indices + top_k_questions_with_indices if
              isinstance(item, tuple) and len(item) > 1]
    config.logger.info(f"Создание корпуса: {time.time() - start_time:.2f} сек.")
    start_time = time.time()
    response = get_ranked_docs(tokenizer, CrossEncoder, new_question, corpus)
    config.logger.info(f"get_ranked_docs: {time.time() - start_time:.2f} сек.")

    return response

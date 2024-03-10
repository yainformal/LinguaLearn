from django.http import JsonResponse

from utils.feature import response_lookup, generate_response
from django.apps import apps
from conf import config

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
import httpx


@method_decorator(csrf_exempt, name='dispatch')
class ResponseLookupView(View):
    async def post(self, request, *args, **kwargs):
        # Получение параметров из запроса
        user_request = json.loads(request.body.decode('utf-8'))
        new_question = user_request.get('new_question')
        app_config = apps.get_app_config('LinguaLearn')
        components = app_config.global_components
        questions_params = components['questions_params']
        answer_params = components['answer_params']
        tokenizer = components['tokenizer']
        CrossEncoder = components['CrossEncoder']

        # Вызов асинхронной функции
        response = await response_lookup(new_question, questions_params, answer_params, tokenizer, CrossEncoder)

        # Возвращение ответа
        return JsonResponse({'response': response})



@method_decorator(csrf_exempt, name='dispatch')
class GenerateResponseLookupView(View):
    async def post(self, request, *args, **kwargs):
        # Получение параметров из запроса
        user_request = json.loads(request.body.decode('utf-8'))
        new_question = user_request.get('new_question')
        history = user_request.get('history', None)
        app_config = apps.get_app_config('LinguaLearn')
        components = app_config.global_components
        model = components['model']
        tokenizer = components['tokenizer']
        generation_options = components['generation_options']
        new_question = str(new_question)

        if history:
        # Вызов асинхронной функции
            response = await generate_response(new_question, tokenizer, model, generation_options, history)
        else:
            response = await generate_response(new_question, tokenizer, model, generation_options)

        # Возвращение ответа
        return JsonResponse({'response': response})



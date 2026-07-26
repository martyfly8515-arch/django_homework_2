import requests

from pathlib import Path

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView

from .models import Product




class HomeView(TemplateView):
    template_name = 'bboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['card'] = {
            'title': 'Django объект',
            'description': (
                'Это карточка объекта, созданная '
                'с помощью HTML и CSS.'
            ),
            'price': 'Бесплатно',
        }

        return context




class TodosView(TemplateView):
    template_name = 'bboard/todos.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        url = 'https://jsonplaceholder.typicode.com/todos/'
        response = requests.get(url, timeout=10)

        context['todos'] = response.json()[:10]

        return context





class ProductActionView(View):

    def get(self, request, product_id, action):
        product = get_object_or_404(
            Product,
            id=product_id
        )

        if action == 'info':
            result = product.get_id_and_name()

        elif action == 'total':
            result = (
                f'Общая сумма: '
                f'{product.get_total_sum()}'
            )

        else:
            result = 'Неизвестное действие'

        return HttpResponse(result)





class TextResponseView(View):
    response_text = ''

    def get(self, request, *args, **kwargs):
        text = self.response_text.format(**kwargs)

        return HttpResponse(text)




class TaskListView(TextResponseView):
    response_text = 'Список всех задач'


class TaskCreateView(TextResponseView):
    response_text = 'Создание новой задачи'


class TaskCompletedView(TextResponseView):
    response_text = 'Список выполненных задач'


class TaskPendingView(TextResponseView):
    response_text = 'Список невыполненных задач'


class TaskSearchView(TextResponseView):
    response_text = 'Поиск задач'


class TaskByPriorityView(TextResponseView):
    response_text = 'Задачи с приоритетом: {priority}'


class TaskDetailView(TextResponseView):
    response_text = 'Просмотр задачи №{task_id}'


class TaskUpdateView(TextResponseView):
    response_text = 'Редактирование задачи №{task_id}'


class TaskDeleteView(TextResponseView):
    response_text = 'Удаление задачи №{task_id}'


class TaskToggleView(TextResponseView):
    response_text = 'Изменение статуса задачи №{task_id}'


class TaskArchiveView(TextResponseView):
    response_text = 'Перемещение задачи №{task_id} в архив'


class TaskRestoreView(TextResponseView):
    response_text = 'Восстановление задачи №{task_id} из архива'




class TasksJsonView(View):

    def get(self, request):
        tasks = [
            {
                'id': number,
                'title': f'Задача {number}',
                'completed': number % 2 == 0,
            }
            for number in range(1, 11)
        ]

        return JsonResponse(
            tasks,
            safe=False,
            json_dumps_params={
                'ensure_ascii': False
            }
        )




class ProtectedPageView(View):

    def write_log(self, request, login):
        log_file = (
            Path(settings.BASE_DIR)
            / 'request_log.txt'
        )

        with log_file.open(
            'a',
            encoding='utf-8'
        ) as file:
            file.write(
                f'Время: {timezone.now()}\n'
                f'Метод запроса: {request.method}\n'
                f'Адрес страницы: {request.path}\n'
                f'GET-данные: {dict(request.GET)}\n'
                f'Логин: {login or "отсутствует"}\n'
                f'User-Agent: '
                f'{request.headers.get("User-Agent", "")}\n'
                '----------------------------------------\n'
            )

    def get(self, request):
        login = request.GET.get('login')

        self.write_log(request, login)

        if not login:
            return redirect('home')

        return HttpResponse(
            f'Пользователь вошёл с логином: {login}'
        )
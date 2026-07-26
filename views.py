import requests

from django.http import HttpResponse, JsonResponse
from pathlib import Path

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Product


def home(request):
    card = {
        'title': 'Django объект',
        'description': 'Это карточка объекта, созданная с помощью HTML и CSS.',
        'price': 'Бесплатно',
    }

    return render(
        request,
        'bboard/home.html',
        {'card': card}
    )


def todos(request):
    url = 'https://jsonplaceholder.typicode.com/todos/'
    response = requests.get(url)
    todos_list = response.json()[:10]

    return render(
        request,
        'bboard/todos.html',
        {'todos': todos_list}
    )


def product_action(request, product_id, action):
    product = get_object_or_404(Product, id=product_id)

    if action == 'info':
        result = product.get_id_and_name()

    elif action == 'total':
        result = f'Общая сумма: {product.get_total_sum()}'

    else:
        result = 'Неизвестное действие'

    return HttpResponse(result)

    # ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ №14
# Контроллеры для приложения «Лист задач»
# ============================================================


def task_list(request):
    return HttpResponse('Список всех задач')


def task_create(request):
    return HttpResponse('Создание новой задачи')


def task_completed(request):
    return HttpResponse('Список выполненных задач')


def task_pending(request):
    return HttpResponse('Список невыполненных задач')


def task_search(request):
    return HttpResponse('Поиск задач')


def task_by_priority(request, priority):
    return HttpResponse(
        f'Задачи с приоритетом: {priority}'
    )


def task_detail(request, task_id):
    return HttpResponse(
        f'Просмотр задачи №{task_id}'
    )


def task_update(request, task_id):
    return HttpResponse(
        f'Редактирование задачи №{task_id}'
    )


def task_delete(request, task_id):
    return HttpResponse(
        f'Удаление задачи №{task_id}'
    )


def task_toggle(request, task_id):
    return HttpResponse(
        f'Изменение статуса задачи №{task_id}'
    )


def task_archive(request, task_id):
    return HttpResponse(
        f'Перемещение задачи №{task_id} в архив'
    )


def task_restore(request, task_id):
    return HttpResponse(
        f'Восстановление задачи №{task_id} из архива'
    )

    # ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ №15
# Формирование списка через list comprehension и JsonResponse
# ============================================================


def tasks_json(request):
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
        json_dumps_params={'ensure_ascii': False}
    )

    # ============================================================
# ДОМАШНЕЕ ЗАДАНИЕ №16
# Перенаправление при отсутствии логина и логирование запроса
# ============================================================


def protected_page(request):
    login = request.GET.get('login')

    log_file = Path(settings.BASE_DIR) / 'request_log.txt'

    with log_file.open('a', encoding='utf-8') as file:
        file.write(
            f'Время: {timezone.now()}\n'
            f'Метод запроса: {request.method}\n'
            f'Адрес страницы: {request.path}\n'
            f'GET-данные: {dict(request.GET)}\n'
            f'Логин: {login or "отсутствует"}\n'
            f'User-Agent: {request.headers.get("User-Agent", "")}\n'
            '----------------------------------------\n'
        )

    if not login:
        return redirect('home')

    return HttpResponse(
        f'Пользователь вошёл с логином: {login}'
    )
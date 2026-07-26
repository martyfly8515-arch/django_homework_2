import requests

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

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
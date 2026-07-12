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
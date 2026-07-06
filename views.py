import requests
from django.shortcuts import render


def home(request):
    card = {
        'title': 'Django объект',
        'description': 'Это карточка объекта, созданная с помощью HTML и CSS.',
        'price': 'Бесплатно',
    }

    return render(request, 'bboard/home.html', {'card': card})


def todos(request):
    url = 'https://jsonplaceholder.typicode.com/todos/'

    response = requests.get(url)
    todos_list = response.json()[:10]

    return render(request, 'bboard/todos.html', {'todos': todos_list})
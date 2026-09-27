from django.shortcuts import render


def products(request):
    products_list = [
        {
            'name': 'Ноутбук',
            'price': 350000,
            'description': 'Ноутбук для работы и учёбы'
        },
        {
            'name': 'Смартфон',
            'price': 180000,
            'description': 'Современный смартфон'
        },
        {
            'name': 'Наушники',
            'price': 25000,
            'description': 'Беспроводные наушники'
        }
    ]

    return render(
        request,
        'practice_36/products.html',
        {'products': products_list}
    )

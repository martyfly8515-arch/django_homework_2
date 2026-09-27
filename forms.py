from django.forms import modelformset_factory

from .models import Product


ProductFormSet = modelformset_factory(
    Product,
    fields=('name', 'price', 'quantity'),
    extra=3
)

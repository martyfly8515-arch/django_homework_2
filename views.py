from django.shortcuts import redirect, render

from .forms import ProductFormSet
from .models import Product


def product_formset(request):
    if request.method == 'POST':
        formset = ProductFormSet(
            request.POST,
            queryset=Product.objects.none()
        )

        if formset.is_valid():
            formset.save()
            return redirect('product_formset')
    else:
        formset = ProductFormSet(
            queryset=Product.objects.none()
        )

    return render(
        request,
        'homework_27/product_formset.html',
        {'formset': formset}
    )

from django.urls import path

from .views import product_formset


urlpatterns = [
    path('', product_formset, name='product_formset'),
]

from django.urls import path

from .views import feedback_form, success


urlpatterns = [
    path('', feedback_form, name='feedback_form'),
    path('success/', success, name='success'),
]

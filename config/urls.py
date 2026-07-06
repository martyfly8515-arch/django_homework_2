from django.contrib import admin
from django.urls import path
from bboard import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),
]
from django.contrib import admin
from django.urls import path, re_path

from bboard import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('todos/', views.todos, name='todos'),

    path(
        'product/<int:product_id>/<str:action>/',
        views.product_action,
        name='product_action'
    ),

    # Обычные маршруты через path()
    path('tasks/', views.task_list, name='task_list'),
    path(
    'tasks/json/',
    views.tasks_json,
    name='tasks_json'
),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/completed/', views.task_completed, name='task_completed'),
    path('tasks/pending/', views.task_pending, name='task_pending'),
    path('tasks/search/', views.task_search, name='task_search'),
    path(
        'tasks/priority/<str:priority>/',
        views.task_by_priority,
        name='task_by_priority'
    ),

    # Маршруты через регулярные выражения
    re_path(
        r'^tasks/(?P<task_id>\d+)/$',
        views.task_detail,
        name='task_detail'
    ),
    re_path(
        r'^tasks/(?P<task_id>\d+)/update/$',
        views.task_update,
        name='task_update'
    ),
    re_path(
        r'^tasks/(?P<task_id>\d+)/delete/$',
        views.task_delete,
        name='task_delete'
    ),
    re_path(
        r'^tasks/(?P<task_id>\d+)/toggle/$',
        views.task_toggle,
        name='task_toggle'
    ),
    re_path(
        r'^tasks/(?P<task_id>\d+)/archive/$',
        views.task_archive,
        name='task_archive'
    ),
    re_path(
        r'^tasks/(?P<task_id>\d+)/restore/$',
        views.task_restore,
        name='task_restore'
    ),
]
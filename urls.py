from django.contrib import admin
from django.urls import path, re_path

from bboard import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path(
        '',
        views.HomeView.as_view(),
        name='home'
    ),

    path(
        'todos/',
        views.TodosView.as_view(),
        name='todos'
    ),

    path(
        'product/<int:product_id>/<str:action>/',
        views.ProductActionView.as_view(),
        name='product_action'
    ),

    path(
        'tasks/',
        views.TaskListView.as_view(),
        name='task_list'
    ),

    path(
        'tasks/json/',
        views.TasksJsonView.as_view(),
        name='tasks_json'
    ),

    path(
        'tasks/create/',
        views.TaskCreateView.as_view(),
        name='task_create'
    ),

    path(
        'tasks/completed/',
        views.TaskCompletedView.as_view(),
        name='task_completed'
    ),

    path(
        'tasks/pending/',
        views.TaskPendingView.as_view(),
        name='task_pending'
    ),

    path(
        'tasks/search/',
        views.TaskSearchView.as_view(),
        name='task_search'
    ),

    path(
        'tasks/priority/<str:priority>/',
        views.TaskByPriorityView.as_view(),
        name='task_by_priority'
    ),

    path(
        'protected/',
        views.ProtectedPageView.as_view(),
        name='protected_page'
    ),

    re_path(
        r'^tasks/(?P<task_id>\d+)/$',
        views.TaskDetailView.as_view(),
        name='task_detail'
    ),

    re_path(
        r'^tasks/(?P<task_id>\d+)/update/$',
        views.TaskUpdateView.as_view(),
        name='task_update'
    ),

    re_path(
        r'^tasks/(?P<task_id>\d+)/delete/$',
        views.TaskDeleteView.as_view(),
        name='task_delete'
    ),

    re_path(
        r'^tasks/(?P<task_id>\d+)/toggle/$',
        views.TaskToggleView.as_view(),
        name='task_toggle'
    ),

    re_path(
        r'^tasks/(?P<task_id>\d+)/archive/$',
        views.TaskArchiveView.as_view(),
        name='task_archive'
    ),

    re_path(
        r'^tasks/(?P<task_id>\d+)/restore/$',
        views.TaskRestoreView.as_view(),
        name='task_restore'
    ),
]
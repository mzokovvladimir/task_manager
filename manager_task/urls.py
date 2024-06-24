from django.urls import path
from . import views
from API_stat.views import TaskListAPIView


urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('api/', TaskListAPIView.as_view(), name='api_list'),
]

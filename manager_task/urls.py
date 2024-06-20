from django.urls import path
from . import views

#потрібна гловна сторінка з якої все буде починатись.
# І реєстрації ще теж немає.

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskStatisticsAPIView, api_overview, TaskViewSet
from API_stat.views import TaskListAPIView

app_name = 'api'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('api-overview/', api_overview, name='api-overview'),
    path('task_list/', TaskListAPIView.as_view(), name='task-list'),
    path('statistics/', TaskStatisticsAPIView.as_view(), name='statistics'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskStatisticsAPIView, api_overview, statistic, task_statistic, TaskViewSet, UserStatisticsAPIView

app_name = 'api'

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')


urlpatterns = [
    path('', include(router.urls)),
    path('api-overview/', api_overview, name='api-overview'),
    path('user-statistics/', TaskStatisticsAPIView.as_view(), name='user-statistics'),
    path('statistics/', UserStatisticsAPIView.as_view(), name='statistics'),
    path('statistic/', statistic, name='statistic'),
    path('task-statistic', task_statistic, name='task-statistic')


]

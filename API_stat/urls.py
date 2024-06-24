from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskStatisticsAPIView, api_overview, TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api_overview/', api_overview, name='api-overview'),
    path('statistics/', TaskStatisticsAPIView.as_view(), name='statistics'),
]

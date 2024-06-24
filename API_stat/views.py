from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from manager_task.models import Task
from .serializers import TaskSerializer, TaskStatisticsSerializer
from django.db.models import Count, Q
from accounts.models import CustomUser


class TaskViewSet(viewsets.ViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListAPIView(APIView):

    @staticmethod
    def get(request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TaskStatisticsAPIView(APIView):

    @staticmethod
    def get(request):
        statistics = CustomUser.objects.annotate(
            total_tasks=Count('task'),
            completed_tasks=Count('task', filter=Q(task__completed=True)),
            pending_tasks=Count('task', filter=Q(task__completed=False))
        )

        min_tasks = request.GET.get('min_tasks', None)
        max_tasks = request.GET.get('max_tasks', None)
        completed = request.GET.get('completed', None)

        if min_tasks is not None:
            statistics = statistics.filter(total_tasks__gte=min_tasks)

        if max_tasks is not None:
            statistics = statistics.filter(total_tasks__lte=max_tasks)

        if completed is not None:
            if completed.lower() == 'true':
                statistics = statistics.filter(completed_tasks__gt=0)
            elif completed.lower() == 'false':
                statistics = statistics.filter(completed_tasks=0)

        serializer = TaskStatisticsSerializer(statistics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def api_overview(request):
    return render(request, 'API/api_overview.html')

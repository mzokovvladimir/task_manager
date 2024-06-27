from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from manager_task.models import Task
from .serializers import TaskSerializer, TaskStatisticsSerializer, UserSerializer
from django.db.models import Count, Q
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.routers import APIRootView


class TaskViewSet(viewsets.ViewSet):
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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskStatisticsViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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


@api_view(['GET'])
def api_overview(request):
    api_root_url = reverse('api:api-root', request=request)
    return render(request, 'API/api_overview.html', {'api_root_url': api_root_url})



@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'id': user.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



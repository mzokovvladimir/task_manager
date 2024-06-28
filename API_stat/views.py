from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from manager_task.models import Task
from .serializers import TaskSerializer, TaskStatisticsSerializer, UserSerializer, UserStatisticsSerializer
from django.db.models import Count, Q
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(Task, pk=kwargs['pk'])
        serializer = TaskSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskStatisticsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        statistics = CustomUser.objects.annotate(
            total_tasks=Count('task'),
            completed_tasks=Count('task', filter=Q(task__completed=True)),
            pending_tasks=Count('task', filter=Q(task__completed=False)),

        )

        min_tasks = request.GET.get('min_tasks')
        max_tasks = request.GET.get('max_tasks')
        completed = request.GET.get('completed')

        if min_tasks:
            statistics = statistics.filter(total_tasks__gte=int(min_tasks))

        if max_tasks:
            statistics = statistics.filter(total_tasks__lte=int(max_tasks))

        if completed is not None:
            if completed.lower() == 'true':
                statistics = statistics.filter(completed_tasks__gt=0)
            elif completed.lower() == 'false':
                statistics = statistics.filter(completed_tasks=0)

        serializer = TaskStatisticsSerializer(statistics, many=True,
                                              context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserStatisticsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('user_id')
        if user_id:
            users = CustomUser.objects.filter(id=user_id)
        else:
            users = CustomUser.objects.all()

        statistics = []
        for user in users:
            user_stats = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'total_tasks': user.task_set.count(),
                'active': user.is_active,
                'staff': user.is_staff,
                'superuser': user.is_superuser,
            }
            statistics.append(user_stats)

        serializer = UserStatisticsSerializer(statistics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def api_overview(request):
    return render(request, 'API/api_overview.html')


def statistic(request):
    return render(request, 'API/statistic.html')


def task_statistic(request):
        return render(request, 'API/task_statistic.html')


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'id': user.pk}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework import serializers
from manager_task.models import Task
from accounts.models import CustomUser


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskStatisticsSerializer(serializers.ModelSerializer):
    total_tasks = serializers.IntegerField()
    completed_tasks = serializers.IntegerField()
    pending_tasks = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'total_tasks', 'completed_tasks', 'pending_tasks']

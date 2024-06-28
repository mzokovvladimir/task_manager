from rest_framework import serializers
from manager_task.models import Task
from accounts.models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'user']
        read_only_fields = ['user']


class UserStatisticsSerializer(serializers.ModelSerializer):
    total_tasks = serializers.IntegerField()
    completed_tasks = serializers.IntegerField()
    pending_tasks = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'total_tasks', 'completed_tasks', 'pending_tasks', 'is_active',
                  'is_staff', 'is_superuser']

    @staticmethod
    def active(obj):
        return obj.is_active

    @staticmethod
    def staff(obj):
        return obj.is_staff

    @staticmethod
    def superuser(obj):
        return obj.is_superuser


class TaskStatisticsSerializer(serializers.ModelSerializer):
    total_tasks = serializers.IntegerField()
    completed_tasks = serializers.IntegerField()
    pending_tasks = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'total_tasks', 'completed_tasks', 'pending_tasks']


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    @staticmethod
    def get_token(obj):
        refresh = RefreshToken.for_user(obj)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'token')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

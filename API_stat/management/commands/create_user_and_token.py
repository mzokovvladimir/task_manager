from accounts.models import CustomUser
from rest_framework.authtoken.models import Token
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create user and token'

    def handle(self, *args, **options):
        user, created = CustomUser.objects.get_or_create(username='custom_user')
        token, created = Token.objects.get_or_create(user=user)
        self.stdout.write(self.style.SUCCESS(f'Token for user {user.username}: {token.key}'))
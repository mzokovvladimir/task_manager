from django.db import models
# from django.contrib.auth.models import User
from accounts.models import CustomUser


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, default=1)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High')))
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'title')

    def __str__(self):
        return self.title

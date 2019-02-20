from django.db import models

from django.db import models
from django.contrib.auth.models import User

class TaskGroup(models.Model):
    task_group_name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='TaskGroups')
    def __str__(self):
        return self.task_group_name

class Task(models.Model):
    task_name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    sequence = models.IntegerField(default=0)
    Task_group = models.ForeignKey(TaskGroup, on_delete=models.CASCADE, related_name='Tasks')
    def __str__(self):
        return self.task_name

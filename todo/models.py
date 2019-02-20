from django.db import models
from django.contrib.auth.models import User

class TodoGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='todogroups')
    def __str__(self):
        return self.name

class Todo(models.Model):
    label = models.CharField(max_length=300)
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sequence = models.IntegerField(default=0)
    todo_group = models.ForeignKey(TodoGroup, on_delete=models.CASCADE, related_name='todos')
    def __str__(self):
        return self.label

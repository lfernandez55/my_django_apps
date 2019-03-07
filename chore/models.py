from django.db import models
from django.contrib.auth.models import User

class ChoreGroup(models.Model):
    choregroup_name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='ChoreGroup')
    def __str__(self):
        return self.choregroup_name

class Chore(models.Model):
    chore_name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    sequence = models.IntegerField(default=0)
    choregroup = models.ForeignKey(ChoreGroup, on_delete=models.CASCADE, related_name='Chore')
    def __str__(self):
        return self.chore_name

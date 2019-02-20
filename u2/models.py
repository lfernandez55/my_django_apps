from django.db import models
from django.utils.text import Truncator

class Presentation(models.Model):
    description = models.TextField(max_length=4000)
    # summary = models.TextField(max_length=500)
    email = models.TextField(max_length=250)
    # firstname = models.TextField(max_length=250)
    # lastname = models.TextField(max_length=250)
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(null=True)
    # created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='posts')
    # updated_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name='+')
    def __str__(self):
        truncated_message = Truncator(self.description)
        return truncated_message.chars(30)

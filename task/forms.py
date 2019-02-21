from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import TaskGroup, Task


class TaskGroupForm(ModelForm):

    class Meta:
        model = TaskGroup
        exclude = ()

class TaskGroupTaskForm(ModelForm):

    class Meta:
        model = Task
        exclude = ()


TaskFormSet = inlineformset_factory(TaskGroup, Task,
                                            form=TaskGroupTaskForm, extra=1)

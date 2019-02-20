from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from .models import TaskGroup
# from .forms import FamilyMemberFormSet


class TaskgroupList(ListView):
    model = TaskGroup

# class TaskgroupCreate(CreateView):
#     model = TaskGroup
#     fields = ['task_group_name', 'description']
#
class TaskgroupTaskCreate(CreateView):
    print('debug')
#
# class TaskgroupUpdate(UpdateView):
#     model = TaskGroup
#     success_url = '/'
#     fields = ['task_group_name', 'description']
#
class TaskgroupTaskUpdate(UpdateView):
    print('debug')
#
# class TaskgroupDelete(DeleteView):
#     model = TaskGroup
#     success_url = reverse_lazy('taskgroup_list')

def TaskgroupDelete(request, taskgroup_id, template_name='task/taskgroup_confirm_delete.html'):
    taskgroup= get_object_or_404(TaskGroup, pk=taskgroup_id)
    if request.method=='POST':
        taskgroup.delete()
        return redirect('taskgroup_list')
    return render(request, template_name, {'object':taskgroup})

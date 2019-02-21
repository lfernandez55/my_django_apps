from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from .models import TaskGroup
from .forms import TaskFormSet
from django.contrib.auth.models import User

class TaskgroupList(ListView):
    model = TaskGroup

    def get_queryset(self):
        queryset = TaskGroup.objects.all().filter(author=self.request.user).order_by('-task_group_name')
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super(TaskgroupList, self).get_context_data(**kwargs)
    #     context['tags'] = Tag.objects.all()
    #     return context

class TaskgroupTaskCreate(CreateView):
    print('debug')
    model = TaskGroup
    fields = ['task_group_name', 'description','author']
    success_url = reverse_lazy('taskgroup_list')

    # this method is called from the form_valid method below
    def get_context_data(self, **kwargs):
        data = super(TaskgroupTaskCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['tasks'] = TaskFormSet(self.request.POST)
        else:
            data['tasks'] = TaskFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        tasks = context['tasks']
        with transaction.atomic():
            self.object = form.save()
            if tasks.is_valid():
                tasks.instance = self.object
                tasks.save()
        return super(TaskgroupTaskCreate, self).form_valid(form)

    def get_initial(self):
        initial = super(TaskgroupTaskCreate, self).get_initial()
        initial = initial.copy()
        initial['author']=self.request.user
        return initial

class TaskgroupUpdate(UpdateView):
    model = TaskGroup
    success_url = '/'
    fields = ['task_group_name', 'description']

class TaskgroupTaskUpdate(UpdateView):
    model = TaskGroup
    fields = ['task_group_name', 'description','author']
    success_url = reverse_lazy('taskgroup_list')

    def get_context_data(self, **kwargs):
        data = super(TaskgroupTaskUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['tasks'] = TaskFormSet(self.request.POST, instance=self.object)
        else:
            data['tasks'] = TaskFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        print('debug here', self.request.user)
        context = self.get_context_data()
        tasks = context['tasks']
        with transaction.atomic():
            self.object = form.save()
            if tasks.is_valid():
                tasks.instance = self.object
                tasks.save()
        return super().form_valid(form)



class TaskgroupDelete(DeleteView):
    model = TaskGroup
    success_url = reverse_lazy('taskgroup_list')

# these might come in handy in the future if i want to move to function based views
# def TaskgroupDelete(request, taskgroup_id, template_name='task/taskgroup_confirm_delete.html'):
#     taskgroup= get_object_or_404(TaskGroup, pk=taskgroup_id)
#     if request.method=='POST':
#         taskgroup.delete()
#         return redirect('taskgroup_list')
#     return render(request, template_name, {'object':taskgroup})

# def TaskgroupTaskCreate(request):
#     if request.method == 'POST':
#         formset = TaskFormSet(data=request.POST)
#         print('debug in updatetodos')
#         if formset.is_valid():
#             print('debug 222 in updatetodos')
#             formset.save()
#         else:
#             print('NOT VALID', formset.errors)
#     formset = TaskFormSet()
#     return render(request, "task/taskgroup_form.html", {"formset": formset })

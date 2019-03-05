from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse, reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from .models import TaskGroup, Task
from .forms import TaskFormSet
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import user_is_taskgroup_author

@method_decorator(login_required, name='dispatch')
class TaskgroupList(ListView):
    model = TaskGroup

    def get_queryset(self):
        queryset = TaskGroup.objects.all().filter(author=self.request.user).order_by('-task_group_name')
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super(TaskgroupList, self).get_context_data(**kwargs)
    #     context['tags'] = Tag.objects.all()
    #     return context

@method_decorator(login_required, name='dispatch')
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

@method_decorator(user_is_taskgroup_author, name='dispatch')
class TaskgroupTaskUpdate(UpdateView):
    model = TaskGroup
    fields = ['task_group_name', 'description','author']
    success_url = reverse_lazy('taskgroup_list')

    def get_context_data(self, **kwargs):
        #     # here is some good documentaton on get_context_data,
        # https://stackoverflow.com/questions/36950416/when-to-use-get-get-queryset-get-context-data-in-django
        # it's used to compute/populate the form
        #     # here im needing to override it on the get call because I want to order the tasks by the sequence
        #     #field.  The View (e.g. UpdateView) isn't smart enough to know on its own that this needs to be done
        #     #notice that it is being called from form_valid which happens on POST
        #     #but the get_context_data method also seems to run automatically on getself.
        #     #the data object that is returned
        #     #from the method is needed on post to save the model and on get to create the form
        data = super(TaskgroupTaskUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['tasks'] = TaskFormSet(self.request.POST, instance=self.object)
        else:
            # Notice here that the "self.object" contains a string like "foo" or whatever
            #the actual name of the TaskGroup is.
            #if one doesn't pass in the queryset the sequence wont be ordered.  This is
            #the only reason it's being passed in.
            querytasks = Task.objects.filter(Task_group__author=self.request.user).filter(Task_group__task_group_name=self.object).order_by('-sequence')
            data['tasks'] = TaskFormSet(instance=self.object,queryset=querytasks)

        return data

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # The default implementation for form_valid() simply redirects to the success_url.
        # which in this case is the page that the user clicked on to get to this form.

        print('debug herrrrrrrrrrrrrrrrrrrrrrrrrrrrrrre', self.request.user)
        context = self.get_context_data()
        tasks = context['tasks']
        with transaction.atomic():
            self.object = form.save()
            if tasks.is_valid():
                tasks.instance = self.object
                tasks.save()
        return super().form_valid(form)

@user_is_taskgroup_author
def foo(request):
    #there doesn't seem to be any difference between what is output by q1 or q2 even
    #though their sql is different when it is dumped out with the print statments below.
    #the sql join is the same. what is different in the sql is the fields that are specified
    #directly after the select statement.  oddly the user email field isn't listed and yet
    #it can still be outputted in the template!
    q1 = Task.objects.select_related('Task_group').filter(Task_group__task_group_name='Foo')
    q2 = Task.objects.filter(Task_group__task_group_name='Foo')
    #q2 = TaskGroup.objects.select_related('author')
    print(dir(UpdateView))
    print(q1.query)
    print('-------------------------------------------------------------------')
    print(q2.query)
    print('-------------------------------------------------------------------')
    print(q1)
    print('-------------------------------------------------------------------')
    print(q2)

    return render(request, 'task/foo.html', {'q1':q1,'q2':q2 })

# def foo(request):
#     myString="foo"
#     print('dddddddddddddddddddddebug')
#     phrases = ['three french hens','two turtle doves','a partridge in a pear tree']
#     return TemplateResponse(request, 'u2/foo.html', { 'myString': myString, 'phrases': phrases })


class TaskgroupDelete(DeleteView):
    model = TaskGroup
    success_url = reverse_lazy('taskgroup_list')


    # return render(request, foo.html, {'your_queryset':your_queryset})
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

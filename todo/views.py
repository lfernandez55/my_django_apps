from django.shortcuts import render
from .models import TodoGroup, Todo
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import NewTodoForm, TodoFormset, TodoModelFormSet
from django.shortcuts import redirect

def index(request):
        return render(request, 'todo/index.html');

def todo_groups(request):
    print('debug here', request.user)
    todo_group_list = TodoGroup.objects.filter(author=request.user)
    # todo_group_list = TodoGroup.objects.all()
    return render(request, 'todo/todogroups.html', {'todo_group_list': todo_group_list})

def groups_and_todos(request):
    #the fields from the TodoGroup model have to have the todo_group prefix. that prefix is defined
    #in the Todo model.  in addition after the prefix one has to put in two dashes. the filter
    #was added so that only the logged in user's groups and todos would display
    groups_and_todos_list = Todo.objects.all().values('label','finished','todo_group__name').filter(todo_group__author=request.user)
    return render(request, 'todo/groups_and_todos.html', {'groups_and_todos_list': groups_and_todos_list})

def todos_by_group(request,todo_group_id):
    #the hyphen before sequence determines whether to order by ascending or descending
    todos = Todo.objects.all().filter(todo_group__id=todo_group_id).order_by('-sequence')
    return render(request, 'todo/todos.html', {'todos': todos, 'todo_group_name': todos[0].todo_group, 'todo_group_id': todo_group_id })

def new_todo(request,todo_group_id):
    #we instantiate the todo_group only so we can add its pk and name to the breadcrumbs in the form
    todo_group = get_object_or_404(TodoGroup, pk=todo_group_id)
    error=""
    if request.method == 'POST':
        form = NewTodoForm(request.POST)
        # see https://simpleisbetterthancomplex.com/series/2017/09/18/a-complete-beginners-guide-to-django-part-3.html#creating-forms-the-right-way
        # in above page search on if form.is_valid():
        # the is_valid method runs validation methods in the class NewTodoForm which is in todo/forms.py.
        # if it isn't valid the is_valid returns a list of errors to the form which are then displayed by templates\includes\form.html
        if form.is_valid():
           label = request.POST['label']
           todo = Todo.objects.create(label=label,todo_group_id=todo_group_id)
           # return todos_by_group(request,todo_group_id)
           return redirect('todo:todos_by_group', todo_group_id=todo_group_id)
        else:
           error="You have an error!"
    else:
        form = NewTodoForm()
    print(form)
    # in an earlier version of this function using the line below I would pass the todo_group_id and then manually add it
    #as a hidden field to the form.  but the group_id is being passed in the url string so this isn't needed. (for example: new_todo/2)
    #notice too that the url string isn't included as an action parameter in form tag. it's left off
    #instead, its already in the address field of the browser when the form is displayed.  in effect its created when
    #the user presses the new todo button which then makes a request to new_todo/2 or new_todo/1 or whatever
    # return render(request, 'todo/new_todo.html', {'todo': todo, 'form': form, 'error': error, 'todo_group_id': todo_group_id })
    return render(request, 'todo/new_todo.html', { 'form': form, 'error': error, 'todo_group': todo_group })

def manage_group_of_todos(request,todo_group_id):
    print('in manage group of todos')
    todos = Todo.objects.all().filter(todo_group__id=todo_group_id).order_by('-sequence')
    return render(request, 'todo/todos.html', {'todos': todos, 'todo_group_name': todos[0].todo_group, 'todo_group_id': todo_group_id })

def create_todos(request, todo_group_id):
    # derived from https://medium.com/@taranjeet/adding-forms-dynamically-to-a-django-formset-375f1090c2b0
    # TODO: revert this so it only allows the creation of new todos.  Right now
    # the below code prepopulates and when those prepopulated fields are modified it creates
    # new todos rather modifying the existing ones
    todo_group = get_object_or_404(TodoGroup, pk=todo_group_id)
    if request.method == 'GET':
        todos = Todo.objects.all().filter(todo_group__id=todo_group_id).order_by('-sequence').values()
        formset = TodoFormset(initial= todos)
    elif request.method == 'POST':
        todos = Todo.objects.all().filter(todo_group__id=todo_group_id).order_by('-sequence').values()
        formset = TodoFormset(request.POST,initial=todos)
        if formset.is_valid():
            for form in formset:
                if form.has_changed():
                    label = form.cleaned_data.get('label')
                    id = form.cleaned_data.get('id')
                    print('dddddddddddddd', id)
                    if label:
                        Todo(label=label,todo_group_id=todo_group_id).save()
            return redirect('todo:todos_by_group', todo_group_id=todo_group_id)
        else:
            print('not valid')
    return render(request, 'todo/todoset.html', {
        'formset': formset, 'todo_group': todo_group
    })

def update_todos(request, todo_group_id):
    # # from https://micropyramid.com/blog/understanding-djangos-model-formsets-in-detail-and-their-advanced-usage/
    todo_group = get_object_or_404(TodoGroup, pk=todo_group_id)
    if request.method == 'POST':
        formset = TodoModelFormSet(data=request.POST)
        print('debug in updatetodos')
        if formset.is_valid():
            print('debug 222 in updatetodos')
            formset.save()
        else:
            print('NOT VALID', formset.errors)
    # else:
    todos = Todo.objects.all().filter(todo_group__id=todo_group_id).order_by('-sequence')
    # print (todos)
    formset = TodoModelFormSet(queryset=todos)
    print('dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
    # print (formset)
    return render(request, "todo/update_todos.html", {"formset": formset,'todo_group': todo_group })
    # return render(request, "todo/todoset.html", {"formset": formset, 'todo_group': todo_group})

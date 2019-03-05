from django.core.exceptions import PermissionDenied
from .models import TaskGroup

def user_is_taskgroup_author(function):
    def wrap(request, *args, **kwargs):
        print ('debug in decoratorssssssssssss')
        print(kwargs['pk'])
        taskgroup = TaskGroup.objects.get(pk=kwargs['pk'])
        if taskgroup.author == request.user:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    return wrap

from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template.response import TemplateResponse
# from django.views import generic
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# from django.conf import settings

def home(request):
    return render(request, 'home.html');
    # return HttpResponse('Hello, World!')

def login_logout_resources(request):
    return render(request, 'registration/resources.html');

def warning(request):
        return render(request, 'u2/warning.html')

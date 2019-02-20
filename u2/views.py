from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewPresentationForm
from .models import Presentation
from django.template.response import TemplateResponse
from django.views import generic
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from django.conf import settings

# def home(request):
#     return render(request, 'home.html');
    # return HttpResponse('Hello, World!')

def index(request):
        return render(request, 'u2/index.html');
        # return HttpResponse('Hello, World!')

def apply(request):
    presentation = get_object_or_404(Presentation, pk=1)
    error=""
    if request.method == 'POST':
        description = request.POST['description']
        email = request.POST['email']
        print ('number of words:', len(description.split()))
        if len(description.split()) > 15:
           # print('Submission is more than 500 words')
           error = 'Submission is more than 15 words'
        elif len(description.split()) < 10:
           # print('Submission is less than 10 words')
           error = 'Submission is less than 10 words'
        else:
           presentation = Presentation.objects.create(description=description,email=email)
           return render(request, 'u2/created.html')
        form = NewPresentationForm()
        return render(request, 'u2/apply.html', {'presentation': presentation, 'form': form,'error': error})
    else:
        form = NewPresentationForm()
    return render(request, 'u2/apply.html', {'presentation': presentation, 'form': form, 'error': error })

def new_presentation_a(request, formType='as_p'):
    presentation = get_object_or_404(Presentation, pk=1)
    if request.method == 'POST':
        form = NewPresentationForm(request.POST)
        if form.is_valid():
            presentation = form.save()
            print('form saved')
            # return redirect('new_presentation_a_done.html', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewPresentationForm()
    return render(request, 'u2/new_presentation_a.html', {'presentation': presentation, 'form': form, 'formType': formType})

def new_presentation_diff_formats(request):
    presentation = get_object_or_404(Presentation, pk=1)
    form = NewPresentationForm()
    return render(request, 'u2/new_presentation_diff_formats.html', {'presentation': presentation, 'form': form})


def presentations(request):
    presentation_list = Presentation.objects.all()
    return render(request, 'u2/presentations.html', {'presentation_list': presentation_list})

class presentations_list_view(generic.ListView):
    model = Presentation
    slug_field = 'product_slug'
    #template inferred (presentation_list.html)

class presentation_detail_view(generic.DetailView):
    model = Presentation
    #template inferred  (presentation_detail.html) (you can override it)

def foo(request):
    myString="foo"
    print('dddddddddddddddddddddebug')
    phrases = ['three french hens','two turtle doves','a partridge in a pear tree']
    return TemplateResponse(request, 'u2/foo.html', { 'myString': myString, 'phrases': phrases })


def presentation(request,presentation_id):
    presentation = Presentation.objects.get(pk=presentation_id)
    return render(request, 'u2/presentation.html', {'presentation': presentation})


@login_required
def protected_view(request):
    return render(request, 'u2/protected_view.html')



def email(request):
    subject = 'test message from django'
    message = 'my test message '
    email_from = 'djangoman34@gmail.com'
    recipient_list = ['luke.fernandez@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return TemplateResponse(request, 'u2/email.html')

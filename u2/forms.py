from django import forms
from .models import Presentation
from django.core.exceptions import ValidationError
# from .models import Post
#
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['message', ]
#
# class NewTopicForm(forms.ModelForm):
#     # message = forms.CharField(widget=forms.Textarea(), max_length=4000)
#     message = forms.CharField(
#         widget=forms.Textarea(
#             attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
#         ),
#         max_length=4000,
#         help_text='The max length of the text is 4000.'
#     )
#
#     class Meta:
#         model = Topic
#         fields = ['subject', 'message']

class NewPresentationForm(forms.ModelForm):


    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 3, 'placeholder': 'Write a desc of your presentation here'}
        ),
        max_length=200,
        help_text='This is where some help text can go...'
    )

    # for an optional field use: email = forms.EmailField(required=False)
    email = forms.CharField(
        widget=forms.TextInput(
        attrs={'placeholder': 'Place your email address here'}
        ),
        max_length=240,
        help_text='The max length of the text is 240.'
    )


    class Meta:
        model = Presentation
        fields = ['description','email' ]

    # see https://stackoverflow.com/questions/7948750/custom-form-validation
    def clean_email(self):
        email = self.cleaned_data['email']
        # if User.objects.filter(email=email).exists():
        if self.cleaned_data['email'] == 'lfernandez@weber.edu':
            raise ValidationError("You may not use lfernandez@weber.edu!!")
        return email

    # use something like this for validating codependent fields
    # see https://stackoverflow.com/questions/7948750/custom-form-validation
    # def clean(self):
    #     form_data = self.cleaned_data
    #     # if form_data['password'] != form_data['password_repeat']:
    #     self._errors["email"] = ["Foo (error in email)"]
    #     self._errors["description"] = ["Bar (error in desc)"]
    #     return form_data

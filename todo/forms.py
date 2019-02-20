from django import forms
from .models import Todo
from django.core.exceptions import ValidationError
from django.forms import (formset_factory, modelformset_factory)

class NewTodoForm(forms.ModelForm):

    label = forms.CharField(
        widget=forms.TextInput(
        attrs={'placeholder': 'Write your todo name here'}
        ),
        max_length=300,
        help_text='The max length of the text is 300.',
        label='Todo name:'
    )

    class Meta:
        model = Todo
        fields = ['label' ]

    def clean_label(self):
        label = self.cleaned_data['label']
        # if User.objects.filter(email=email).exists():
        if self.cleaned_data['label'] == 'xxxx':
            raise ValidationError("You may not call your todo 'xxxx'")
        return label

# TodoFormset = formset_factory(NewTodoForm, extra=2)
TodoFormset = formset_factory(NewTodoForm)

# TodoModelFormSet = modelformset_factory(Todo, exclude=['sequence'], can_delete=True, can_order=True)
# TodoModelFormSet = modelformset_factory(Todo, exclude=['todo_group'], can_delete=True,extra=1)
# TodoModelFormSet = modelformset_factory(Todo, exclude=(), can_delete=True,extra=1)
TodoModelFormSet = modelformset_factory(
Todo,
exclude=['finished'],
can_delete=True,
extra=1,
widgets={'sequence': forms.TextInput(attrs={'size': 1})
},

)

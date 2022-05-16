from django import forms
from .models import Event


class AddEvent(forms.ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'description', ]

from django import forms
from .models import SubTask

class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['title', 'complete']

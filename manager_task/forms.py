from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control datepicker',
                'placeholder': 'YYYY-MM-DD',
                'style': 'width: 30%; height: auto; margin: 0 auto;'
            }
        )
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority']


class EditTaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control datepicker',
                'placeholder': 'YYYY-MM-DD',
                'style': 'width: 30%; height: auto; margin: 0 auto;'
            }
        )
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'completed']

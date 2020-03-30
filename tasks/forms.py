from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title',)
        labels = {
            'title': False
        }
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control mr-sm-2',
                    'placeholder': 'Enter a new task',
                    'id': 'new_task',
                }
            )
        }
from django.forms import ModelForm
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django import forms
from .models import Task, Project


#Create Model Form for Task
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "due_date": DatePickerInput(),
        }


#Create Model Form for Project
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        widgets = {
            "start_date": DatePickerInput(),
        }

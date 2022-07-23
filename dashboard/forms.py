from django import forms
from django.forms import fields, widgets
from .models import *

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["title"]

class DateInput(forms.DateInput):
    input_type = "date"

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {"due":DateInput()}
        fields = ["subject","description","due"]

class ExammarkForm(forms.ModelForm):
    class Meta:
        model = Exammarks
        fields = ["subject","firstExam","secondExam","final"]

class TimeInput(forms.TimeInput):
    input_type = "time"

class ExamcalendarForm(forms.ModelForm):
    class Meta:
        model = Examcalendar
        widgets = {"examDate":DateInput(),"examHour":TimeInput()}
        fields = ["subject","examDate","examHour"]

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ["title", "content"]
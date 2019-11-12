from django import forms
from habit_tracker.models import Habit, Entry
from django.forms import ModelForm


class HabitForm(forms.ModelForm):

  class Meta:
    model = Habit
    fields = ['habit_name', 'target_goal', 'measurement']

class EntryForm(forms.ModelForm):

  class Meta:
    model = Entry
    fields = ['habit', 'actual', 'comment']

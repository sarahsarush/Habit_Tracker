# habits/forms.py
from django import forms
from .models import Habit, DailyProgress

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ('name', 'description')

class DailyProgressForm(forms.ModelForm):
    class Meta:
        model = DailyProgress
        fields = ('date',)
        # fields = ('date', 'progress')
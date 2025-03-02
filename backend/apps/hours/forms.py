# apps/hours/forms.py
from django import forms
from .models import HourLog

class HourLogForm(forms.ModelForm):
    class Meta:
        model = HourLog
        fields = ['user', 'activity', 'date', 'hours', 'notes']  # Adjust as needed

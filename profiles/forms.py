from django import forms
from .models import GameEntry

class GameEntryForm(forms.ModelForm):
    class Meta:
        model = GameEntry
        fields = [
            "title",
            "platform",
            "status",
            "date_started",
            "date_completed",
        ]
        widgets = {
            "date_started": forms.DateInput(attrs={"type": "date"}),
            "date_completed": forms.DateInput(attrs={"type": "date"}),
        }

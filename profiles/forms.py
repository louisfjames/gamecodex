from django import forms
from .models import GameEntry

class GameEntryForm(forms.ModelForm):
    
    platform = forms.ChoiceField(choices=(), required=True)
    
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].disabled = True
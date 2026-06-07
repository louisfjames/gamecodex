from django import forms
from .models import GameEntry
from datetime import date


class GameEntryForm(forms.ModelForm):
    """
    A form for creating and updating GameEntry instances, with custom
    validation rules applied to ensure date fields remain consistent
    with the selected game status.

    On initialisation, the title field is set to read-only, and the
    platform field is defined so that choices can be populated dynamically
    by the view. The clean() method enforces several rules: start dates
    cannot be in the future, completion dates cannot precede start dates,
    completed games must include both dates, playing games cannot include
    a completion date, backlog games cannot include any dates, and
    abandoned games cannot include a completion date.

    Returns:
        dict: The cleaned form data after validation, with any field
        errors added where rules are violated.
    """

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
        self.fields["title"].widget.attrs["readonly"] = True

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        date_started = cleaned_data.get("date_started")
        date_completed = cleaned_data.get("date_completed")

        # Rule 1: Start date cannot be in the future
        if date_started and date_started > date.today():
            self.add_error(
                "date_started",
                "Start date cannot be in the future."
            )
            return cleaned_data  # stop further validation

        # Rule 2: Completion date cannot be before start date
        if date_started and date_completed and date_completed < date_started:
            self.add_error(
                "date_completed",
                "Completion date cannot be before the start date."
            )
            return cleaned_data

        # Rule 3: If completed, must have both dates
        if status == "completed":
            if not date_started:
                self.add_error(
                    "date_started",
                    "You must enter a start date for a completed game."
                )
                return cleaned_data
            if not date_completed:
                self.add_error(
                    "date_completed",
                    "You must enter a completion date for a completed game."
                )
                return cleaned_data

        # Rule 4: If playing, cannot have a completion date
        if status == "playing" and date_completed:
            self.add_error(
                "date_completed",
                "A game you're currently playing cannot have"
                " a completion date."
            )
            return cleaned_data

        # Rule 5: If backlog, no dates allowed
        if status == "backlog" and (date_started or date_completed):
            self.add_error(
                "status",
                "Backlog games cannot have start or completion dates."
            )
            return cleaned_data

        # Rule 6: If abandoned, cannot have a completion date
        if status == "abandoned" and date_completed:
            self.add_error(
                "date_completed",
                "Abandoned games cannot have a completion date."
            )
            return cleaned_data

        return cleaned_data

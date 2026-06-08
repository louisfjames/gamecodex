from django.test import TestCase
from datetime import date, timedelta
from profiles.forms import GameEntryForm


class GameEntryFormTests(TestCase):
    """Tests for GameEntryForm validation rules."""

    def get_form(self, overrides=None):
        """Return a form instance with platform choices set."""
        data = {
            "title": "Zelda",
            "platform": "130",
            "status": "completed",
            "date_started": date.today() - timedelta(days=10),
            "date_completed": date.today(),
        }
        if overrides:
            data.update(overrides)
        form = GameEntryForm(data=data)
        form.fields["platform"].choices = [("130", "Switch")]
        return form

    # Rule 1: Start date cannot be in the future
    def test_start_date_in_future_is_invalid(self):
        """Start date in the future should fail validation."""
        form = self.get_form({
            "date_started": date.today() + timedelta(days=1)
        })
        self.assertFalse(form.is_valid())
        self.assertIn("date_started", form.errors)

    # Rule 2: Completion date cannot be before start date
    def test_completion_before_start_is_invalid(self):
        """Completion date before start date should fail validation."""
        form = self.get_form({
            "date_started": date.today() - timedelta(days=5),
            "date_completed": date.today() - timedelta(days=10),
        })
        self.assertFalse(form.is_valid())
        self.assertIn("date_completed", form.errors)

    # Rule 3: Completed games must have both dates
    def test_completed_without_start_date_is_invalid(self):
        """Completed status without a start date should fail validation."""
        form = self.get_form({
            "status": "completed",
            "date_started": None,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("date_started", form.errors)

    def test_completed_without_completion_date_is_invalid(self):
        """
        Completed status without a completion date should fail validation.
        """
        form = self.get_form({
            "status": "completed",
            "date_completed": None,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("date_completed", form.errors)

    def test_completed_with_both_dates_is_valid(self):
        """Completed status with both dates should pass validation."""
        form = self.get_form()
        self.assertTrue(form.is_valid())

    # Rule 4: Playing cannot have a completion date
    def test_playing_with_completion_date_is_invalid(self):
        """Playing status with a completion date should fail validation."""
        form = self.get_form({
            "status": "playing",
            "date_completed": date.today(),
        })
        self.assertFalse(form.is_valid())
        self.assertIn("date_completed", form.errors)

    def test_playing_without_completion_date_is_valid(self):
        """Playing status without a completion date should pass validation."""
        form = self.get_form({
            "status": "playing",
            "date_completed": None,
        })
        self.assertTrue(form.is_valid())

    # Rule 5: Backlog cannot have any dates
    def test_backlog_with_start_date_is_invalid(self):
        """Backlog status with a start date should fail validation."""
        form = self.get_form({
            "status": "backlog",
            "date_started": date.today() - timedelta(days=5),
            "date_completed": None,
        })
        self.assertFalse(form.is_valid())
        self.assertIn("status", form.errors)

    def test_backlog_with_no_dates_is_valid(self):
        """Backlog status with no dates should pass validation."""
        form = self.get_form({
            "status": "backlog",
            "date_started": None,
            "date_completed": None,
        })
        self.assertTrue(form.is_valid())

    # Rule 6: Abandoned cannot have a completion date
    def test_abandoned_with_completion_date_is_invalid(self):
        """Abandoned status with a completion date should fail validation."""
        form = self.get_form({
            "status": "abandoned",
            "date_completed": date.today(),
        })
        self.assertFalse(form.is_valid())
        self.assertIn("date_completed", form.errors)

    def test_abandoned_without_completion_date_is_valid(self):
        """
        Abandoned status without a completion date should pass validation.
        """
        form = self.get_form({
            "status": "abandoned",
            "date_completed": None,
        })
        self.assertTrue(form.is_valid())

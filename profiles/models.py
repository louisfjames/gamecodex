from django.db import models
from django.contrib.auth.models import User

class GameEntry(models.Model):
    """
    Represents a game library entry for a specific user.

    Stores a game's title, platform, and cover image as sourced from IGDB,
    along with the user's personal tracking data such as status and dates.
    Each entry is tied to a single user and a single platform, and neither
    the title nor platform can be changed after the entry is created.

    Attributes:
        user (User): The user who owns this entry.
        title (str): The game title sourced from IGDB.
        platform (str): The platform ID selected during the add flow.
        status (str): The user's current progress status. Must be one of
            'playing', 'completed', 'backlog', or 'abandoned'.
        cover_id (str): The IGDB cover image ID used to display artwork.
        date_added (date): Set automatically when the entry is first created.
        date_started (date): Optionally recorded by the user.
        date_completed (date): Optionally recorded by the user.
        date_modified (datetime): Updated automatically on every save.
    """

    STATUS_CHOICES = [
        ('playing', 'Currently Playing'),
        ('completed', 'Completed'),
        ('backlog', 'Backlog'),
        ('abandoned', 'Abandoned'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    cover_id = models.CharField(max_length=50, blank=True, null=True)

    date_added = models.DateField(auto_now_add=True)
    date_started = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
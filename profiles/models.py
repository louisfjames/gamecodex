from django.db import models
from django.contrib.auth.models import User

class GameEntry(models.Model):
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

    date_added = models.DateField(auto_now_add=True)
    date_started = models.DateField(null=True, blank=True)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.get_status_display()})"
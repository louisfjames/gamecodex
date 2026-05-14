from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path("add/", views.add_game_view, name="add_game"),
]

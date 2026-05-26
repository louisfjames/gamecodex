from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile'),
    path("add/", views.add_game_view, name="add_game"),
    path("entries/", views.all_entries_view, name="all_entries"),
    path('remove/<int:entry_id>/', views.remove_entry, name='remove_entry'),
    path("edit/<int:entry_id>/", views.edit_entry, name="edit_entry"),
]

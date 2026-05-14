from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_game_view, name="add_game"),
    path('', views.search_view, name='search'),
]

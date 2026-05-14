from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GameEntryForm

@login_required
def profile_view(request):
    return render(request, 'profiles/profile.html')

@login_required
def add_game_view(request):
    initial = {}
    title = request.GET.get("title")
    if title:
        initial["title"] = title

    if request.method == "POST":
        form = GameEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect("profile")
    else:
        form = GameEntryForm(initial=initial)

    return render(request, "profiles/add_game.html", {"form": form})
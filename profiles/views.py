from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GameEntryForm
from games.services.igdb import PLATFORM_LOOKUP

@login_required
def profile_view(request):
    return render(request, 'profiles/profile.html')

@login_required
def add_game_view(request):

    # Read values passed from search page
    title = request.GET.get("title")
    platform_ids = request.GET.get("platforms", "")
    cover_id = request.GET.get("cover")
    summary = request.GET.get("summary")



    # Covert platform IDs
    platform_ids = [int(pid) for pid in platform_ids.split(",") if pid]

    platform_choices = [
        (pid, PLATFORM_LOOKUP.get(pid, f"ID {pid}"))
        for pid in platform_ids
    ]

    # Build inital form
    initial = {}
    if title:
        initial["title"] = title

    # Handle POST (saving the entry)
    if request.method == "POST":
        form = GameEntryForm(request.POST)
        form.fields["platform"].choices = platform_choices

        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect("profile")
    else:
        form = GameEntryForm(initial=initial)
        form.fields["platform"].choices = platform_choices

    return render(request, "profiles/add_game.html", {"form": form, "cover_id": cover_id, "summary": summary,})
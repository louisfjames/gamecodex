from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GameEntryForm
from .models import GameEntry
from games.services.igdb import PLATFORM_LOOKUP
from django.contrib import messages

@login_required
def profile_view(request):
    return render(request, 'profiles/profile.html')

@login_required
def add_game_view(request):

    # Read values passed from search page
    title = request.GET.get("title")
    platform_ids = request.GET.get("platforms", "")
    cover_id = request.GET.get("cover") or request.POST.get("cover_id")
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
            entry.cover_id = cover_id
            entry.save()
            
            # Success message displayed on profile page
            list_name = entry.status.capitalize()
            messages.success(request, f"'{entry.title}' has been added to your {list_name} list!")

            return redirect("profile")
    else:
        form = GameEntryForm(initial=initial)
        form.fields["platform"].choices = platform_choices

    return render(request, "profiles/add_game.html", {"form": form, "cover_id": cover_id, "summary": summary,})

@login_required
def all_entries_view(request):
    entries = GameEntry.objects.filter(user=request.user).order_by("-date_added", "status")
    return render(request, "profiles/all_entries.html", {"entries": entries})

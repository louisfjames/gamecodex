from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GameEntryForm
from .models import GameEntry
from games.services.igdb import PLATFORM_LOOKUP
from django.contrib import messages
from django.views.decorators.http import require_POST

@login_required
def profile_view(request):
    """
    Display the user's profile page with a summary of their game activity.

    This view retrieves the latest three GameEntry records for each status category belonging to the authenticated user. These categories include:
    - currently_playing
    - completed
    - backlog
    - abandoned

    The entries are ordered by date_added (newest first) and passed to the template so the profile page can show a quick snapshot of the user's most recent activity in each list.
    """
    user = request.user
    
    entries = GameEntry.objects.filter(user=user)

    currently_playing_entries = entries.filter(status="playing").order_by("-date_added")[:3]

    completed_entries = entries.filter(status="completed").order_by("-date_added")[:3]

    backlog_entries = entries.filter(status="backlog").order_by("-date_added")[:3]

    abandoned_entries = entries.filter(status="abandoned").order_by("-date_added")[:3]

    context = {
        "currently_playing_entries": currently_playing_entries,
        "completed_entries": completed_entries,
        "backlog_entries": backlog_entries,
        "abandoned_entries": abandoned_entries,
    }

    return render(request, 'profiles/profile.html', context)

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
            
            # Duplicate check 
            duplicate_exists = GameEntry.objects.filter(user=request.user, title=form.cleaned_data["title"], platform=form.cleaned_data["platform"]).exists()

            if duplicate_exists:
                form.add_error(None, "You've already added this game to your list.")
                return render(request, "profiles/add_game.html", {"form": form, "cover_id": cover_id, "summary": summary})

            # Save new entry
            entry = form.save(commit=False)
            entry.user = request.user
            entry.cover_id = cover_id
            entry.save()
            
            # Success message displayed on profile page
            list_name = entry.status.capitalize()
            messages.success(request, f"'{entry.title}' has been added to your {list_name} list!", extra_tags="game")

            return redirect("profile")
    else:
        form = GameEntryForm(initial=initial)
        form.fields["platform"].choices = platform_choices

    return render(request, "profiles/add_game.html", {"form": form, "cover_id": cover_id, "summary": summary,})

@login_required
def all_entries_view(request):
    # Read status from the URL
    status = request.GET.get("status")

    # Base queryset
    entries = GameEntry.objects.filter(user=request.user)

    # Apply filter only if a status was selected
    if status:
        entries = entries.filter(status=status)

    # Ordering by date added
    entries = entries.order_by("-date_added", "status")

    # Attach readable platform names
    for entry in entries:
        if entry.platform and entry.platform.isdigit():
            entry.platform_name = PLATFORM_LOOKUP.get(int(entry.platform), entry.platform)
        else:
            entry.platform_name = entry.platform

    # Get status choices from the model
    status_choices = GameEntry._meta.get_field("status").choices

    return render(request, "profiles/all_entries.html", {"entries": entries, "status_choices": status_choices, "current_status": status,})

    
@require_POST
def remove_entry(request, entry_id):
    entry = get_object_or_404(GameEntry, id=entry_id, user=request.user)
    title = entry.title
    entry.delete()
    messages.success(request, f"'{title}' has been removed from your profile.")
    return redirect('all_entries')
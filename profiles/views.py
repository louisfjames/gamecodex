from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import GameEntryForm
from .models import GameEntry
from games.services.igdb import PLATFORM_LOOKUP
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator


@login_required
def profile_view(request):
    """
    Display the user's profile page with a summary of their game activity.

    Retrieves the three most recent GameEntry records for each status category
    belonging to the current user, ordered by date_added descending. These
    snapshots are passed to the template to give the user a quick overview of
    their most recent activity across all four lists.

    Parameters:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: The rendered profile page containing the four entry
        querysets as context.

    Context:
        currently_playing_entries (QuerySet): Up to 3 most recent playing entries.
        completed_entries (QuerySet): Up to 3 most recent completed entries.
        backlog_entries (QuerySet): Up to 3 most recent backlog entries.
        abandoned_entries (QuerySet): Up to 3 most recent abandoned entries.
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
    """
    Display and process the form for adding a new game to the user's library.

    On GET, reads game metadata passed as query parameters from the search page
    and renders a pre-filled form with the title and available platform choices.
    On POST, validates the form, checks for duplicate entries, and saves the new
    GameEntry to the database before redirecting to the user's profile.

    Parameters:
        request (HttpRequest): The incoming HTTP request. On GET, expects the
            following query parameters:
            - 'title' (str): The game title sourced from IGDB.
            - 'platforms' (str): A comma-separated string of IGDB platform IDs.
            - 'cover' (str): The IGDB cover image ID.
            - 'summary' (str): A short description of the game from IGDB.

    Returns:
        HttpResponse: The rendered add game form on GET, or on a failed POST
        validation or duplicate check. Redirects to the profile page on a
        successful save.

    Context:
        form (GameEntryForm): The form instance for creating a new entry.
        cover_id (str): The IGDB cover image ID for displaying artwork.
        summary (str): The game summary sourced from IGDB.
    """

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
    """
    Display all game library entries for the authenticated user.

    Retrieves all GameEntry records belonging to the current user, with an
    optional status filter applied via a GET parameter. Results are ordered
    by date_added descending, then by status. Each entry is annotated with a
    human-readable platform name resolved from PLATFORM_LOOKUP before being
    passed to the template.

    Parameters:
        request (HttpRequest): The incoming HTTP request. Accepts an optional
            GET parameter:
            - 'status' (str): Filters results to a specific status category.
              Must match one of the STATUS_CHOICES values ('playing',
              'completed', 'backlog', 'abandoned').

    Returns:
        HttpResponse: The rendered entries list page.

    Context:
        entries (QuerySet): All matching GameEntry records for the user,
            each annotated with a platform_name attribute.
        status_choices (list): The full list of status choices from the
            GameEntry model, used to populate the filter UI.
        current_status (str or None): The currently active status filter,
            or None if no filter is applied.
    """
    
    # Read status from the URL
    status = request.GET.get("status")

    # Base queryset
    entries = GameEntry.objects.filter(user=request.user)

    # Apply filter only if a status was selected
    if status:
        entries = entries.filter(status=status)

    # Ordering by date added
    entries = entries.order_by("-date_added", "status")

    # Pagination
    paginator = Paginator(entries, 10)  # 10 entries per page
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    # Attach readable platform names
    for entry in page_obj:
        if entry.platform and entry.platform.isdigit():
            entry.platform_name = PLATFORM_LOOKUP.get(int(entry.platform), entry.platform)
        else:
            entry.platform_name = entry.platform  

    # Get status choices from the model
    status_choices = GameEntry._meta.get_field("status").choices

    return render(request, "profiles/all_entries.html", {
        "entries": page_obj, 
        "status_choices": status_choices, 
        "current_status": status,
        "page_obj": page_obj,    
    })


@login_required
@require_POST
def remove_entry(request, entry_id):
    """
    Delete a GameEntry from the authenticated user's library.

    Retrieves the specified entry, ensuring it belongs to the current user,
    then permanently deletes it. A success message is shown and the user is
    redirected back to the full entries list.

    Parameters:
        request (HttpRequest): The incoming HTTP request. Must be a POST request.
        entry_id (int): The ID of the GameEntry to delete.

    Returns:
        HttpResponse: A redirect to the entries list after a successful deletion.
    """

    entry = get_object_or_404(GameEntry, id=entry_id, user=request.user)
    title = entry.title
    entry.delete()
    messages.success(request, f"'{title}' has been removed from your profile.")
    return redirect('all_entries')


@login_required
def edit_entry(request, entry_id):

    """
    Allow the authenticated user to update an existing GameEntry.

    This view retrieves the specified entry, ensuring it belongs to the
    current user, and displays a form pre‑filled with the entry's data.
    On POST, the submitted form is validated and the entry is updated
    in the database. A success message is shown and the user is redirected
    back to the full entries list. On GET, the form is rendered for editing.

    Parameters:
        request (HttpRequest): The incoming HTTP request.
        entry_id (int): The ID of the GameEntry to edit.

    Returns:
        HttpResponse: The rendered edit form on GET, or a redirect to the
        entries list after a successful update.
    """

    entry = get_object_or_404(GameEntry, id=entry_id, user=request.user)
    
    platform_choices = [(pid, name) for pid, name in PLATFORM_LOOKUP.items()]
    
    if request.method == "POST":
        form = GameEntryForm(request.POST, instance=entry)
        form.fields.pop("title", None)
        form.fields.pop("platform", None)
        
        if form.is_valid():
            game_entry = form.save(commit=False)
            game_entry.title = entry.title
            game_entry.platform = entry.platform
            game_entry.save()
            messages.success(request, f"'{entry.title}' has been updated.", extra_tags="game")
            return redirect("all_entries")
    else:
        form = GameEntryForm(instance=entry)
        form.fields["platform"].choices = platform_choices
        form.fields["platform"].widget.attrs["disabled"] = True

    entry.platform_name = PLATFORM_LOOKUP.get(int(entry.platform), entry.platform)
    return render(request, "profiles/edit_entry.html", {"form": form, "entry": entry})

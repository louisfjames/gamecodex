from django.shortcuts import render
from .services.igdb import search_games, PLATFORM_LOOKUP

def search_view(request):
    """
    Handle game search requests and render the search results page.

    On a GET request with query parameters, calls the IGDB search API via
    search_games() and resolves each result's platform IDs to human-readable
    names using PLATFORM_LOOKUP. On a GET request with no parameters (i.e.
    the user has just navigated to the search page), an empty results list
    is returned with no API call made.

    Parameters:
        request (HttpRequest): The incoming HTTP request. Expects optional
        GET parameters 'q' (search query string) and 'platform' (platform
        ID to filter results).

    Returns:
        HttpResponse: The rendered search page with the query, platform filter,
        any API error, and the list of matching game results.
    """
    
    query = request.GET.get("q", "")
    platform = request.GET.get("platform")

    response = {"error": None, "results": []}
    if request.GET:
        response = search_games(query, platform=platform)

        for g in response["results"]:
            g["platform_names"] = [
                PLATFORM_LOOKUP.get(pid, f"ID {pid}") for pid in g.get("platforms", [])
            ]
            
    return render(request, "games/search.html", {
        "query": query,
        "platform": platform,
        "error": response["error"],
        "results": response["results"],
    })

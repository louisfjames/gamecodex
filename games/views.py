from django.shortcuts import render
from .services.igdb import search_games, PLATFORM_LOOKUP

def search_view(request):
    query = request.GET.get("q", "")
    platform = request.GET.get("platform")

    response = {"error": None, "results": []}
    if query:
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

from django.shortcuts import render
from .services.igdb import search_games

def search_view(request):
    query = request.GET.get("q", "")
    platform = request.GET.get("platform")

    response = {"error": None, "results": []}
    if query:
        response = search_games(query, platform=platform)

    return render(request, "games/search.html", {
        "query": query,
        "platform": platform,
        "error": response["error"],
        "results": response["results"],
    })

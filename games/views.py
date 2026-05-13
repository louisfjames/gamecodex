from django.shortcuts import render
from .services.igdb import search_games

def search_view(request):
    query = request.GET.get("q", "")
    response = search_games(query)

    return render(request, "games/search.html", {
        "query": query,
        "error": response["error"],
        "results": response["results"],
    })

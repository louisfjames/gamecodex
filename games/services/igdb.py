import os
import requests

CLIENT_ID = os.environ.get("IGDB_CLIENT_ID")
ACCESS_TOKEN = os.environ.get("IGDB_ACCESS_TOKEN")

PLATFORM_IDS = {
    "PlayStation": [7, 8, 9, 48, 167, 38, 46], # IGDB IDs for PS1 to PS5 and handheld (PSP & Vita_
    "Xbox": [11, 12, 49, 169], # IGDB IDs for Xbox to Series X/S
    "Nintendo": [130, 41, 5, 21, 4, 19, 18, 20, 37], # IGDB IDs for NES to Switch and handheld (DS & 3DS)
    "PC": [6],
}

def search_games(query, platform=None):
    """
    IGDB search function.
    Sends a search query to IGDB and returns raw JSON.
    Defensive design includes: input validation, credential validation, network error handling and non-200 response handling.
    """

    # Input Validation
    if not query or len(query.strip()) < 2:
        return {"error": "Search term must be at least 2 characters.", "results": []}

    # Credential Validation
    if not CLIENT_ID or not ACCESS_TOKEN:
        return {"error": "IGDB credentials missing.", "results": []}

        
    # Base APICalypse Query
    query_string = f'search "{query}"; fields name, cover.image_id, platforms, summary, total_rating, rating;'

    # Platform filtering
    if platform and platform in PLATFORM_IDS:
        ids = PLATFORM_IDS[platform]
        id_string = ",".join(map(str, ids))
        query_string += f" where platforms = ({id_string});"

    # Ending Query String w/ Limit
    query_string += " limit 20;"

    # API Request Setup
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }

    # API Request Error Handling
    try:
        response = requests.post(url, headers=headers, data=query_string, timeout=5)

        if response.status_code != 200:
            return {
                "error": f"IGDB returned status {response.status_code}",
                "results": []
            }

        results = response.json()

        # Sort by popularity
        results = sorted(
            results,
            key=lambda g: g.get("total_rating", g.get("rating", 0)),
            reverse=True
        )

        return {"error": None, "results": results}

    except requests.exceptions.RequestException:
        return {"error": "Network error contacting IGDB.", "results": []}
import os
import requests

CLIENT_ID = os.environ.get("IGDB_CLIENT_ID")
ACCESS_TOKEN = os.environ.get("IGDB_ACCESS_TOKEN")

def search_games(query):
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

    # API Request Setup
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    body = f'search "{query}"; fields name, cover.image_id, summary; limit 20;'

    # API Request Error Handling
    try:
        response = requests.post(url, headers=headers, data=body, timeout=5)

        if response.status_code != 200:
            return {
                "error": f"IGDB returned status {response.status_code}",
                "results": []
            }

        return {"error": None, "results": response.json()}

    except requests.exceptions.RequestException:
        return {"error": "Network error contacting IGDB.", "results": []}
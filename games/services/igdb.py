import os
import requests

CLIENT_ID = os.environ.get("IGDB_CLIENT_ID")
ACCESS_TOKEN = os.environ.get("IGDB_ACCESS_TOKEN")

PLATFORM_IDS = {
    "PlayStation": [7, 8, 9, 48, 167, 38, 46], # IGDB IDs for PS1 to PS5 and handheld (PSP & Vita)
    "Xbox": [11, 12, 49, 169], # IGDB IDs for Xbox to Series X/S
    "Nintendo": [130, 41, 5, 21, 4, 19, 18, 20, 37], # IGDB IDs for NES to Switch and handheld (DS & 3DS)
    "PC": [6],
}

PLATFORM_LOOKUP = {
    7: "PS1",
    8: "PS2",
    9: "PS3",
    48: "PS4",
    167: "PS5",
    38: "PSP",
    46: "PS Vita",

    11: "Xbox",
    12: "Xbox 360",
    49: "Xbox One",
    169: "Xbox Series X/S",

    130: "Switch",
    41: "Wii U",
    5: "Wii",
    21: "GameCube",
    4: "N64",
    19: "SNES",
    18: "NES",
    20: "DS",
    37: "3DS",

    6: "PC",
}

def search_games(query, platform=None, offset=0):
    """
    Search for games via the IGDB API and return results sorted by popularity.

    Constructs an APICalypse query and sends it to the IGDB games endpoint.
    Results include each game's name, cover image, platforms, summary, and
    rating data, and are sorted by total_rating descending (falling back to
    rating where total_rating is absent).

    Parameters:
        query (str): The search term entered by the user. Must be at least
            2 characters after stripping whitespace.
        platform (str, optional): A platform filter key corresponding to an
            entry in PLATFORM_IDS. When provided, restricts results to games
            available on that platform. Defaults to None (no filtering).

    Returns:
        dict: A dictionary with two keys:
            - 'error' (str or None): A human-readable error message if
              something went wrong, otherwise None.
            - 'results' (list): A list of game dictionaries returned by IGDB,
              sorted by popularity. Empty if an error occurred.

    Error conditions:
        - Query is empty or fewer than 2 characters.
        - IGDB credentials (CLIENT_ID or ACCESS_TOKEN) are missing.
        - IGDB returns a non-200 status code.
        - A network error occurs during the request.
    """

    # Input Validation
    if not query or len(query.strip()) < 2:
        return {"error": "Search term must be at least 2 characters.", "results": []}

    # Credential Validation
    if not CLIENT_ID or not ACCESS_TOKEN:
        return {"error": "IGDB credentials missing.", "results": []}
        
    # Base APICalypse Query
    query_string = (f'search "{query}"; fields name, cover.image_id, platforms, summary, total_rating, rating;')

    # Platform filtering
    if platform and platform in PLATFORM_IDS:
        ids = PLATFORM_IDS[platform]
        id_string = ",".join(map(str, ids))
        query_string += f" where platforms = ({id_string});"

    # Ending Query String w/ Limit
    query_string += f" limit 20; offset {offset};"

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
        return {
            "error": "Network error contacting IGDB.", 
            "results": []
        }
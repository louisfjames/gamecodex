import os
import requests

CLIENT_ID = os.environ.get("IGDB_CLIENT_ID")
ACCESS_TOKEN = os.environ.get("IGDB_ACCESS_TOKEN")

def search_games(query):
    url = "https://api.igdb.com/v4/games"
    headers = {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    }
    body = f'search "{query}"; fields name, cover.image_id, summary; limit 20;'

    response = requests.post(url, headers=headers, data=body)
    return response.json()

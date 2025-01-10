CLIENT_ID = "my client id goes here"

CLIENT_SECRET = "my client secret goes here"

import requests
import base64
import json
import pandas as pd
import time

file_path = "/Users/tuanadurmus/Desktop/Spotify_Data.txt"

with open(file_path, "r", encoding="utf-8") as file:
    spotify_data = json.load(file)


def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + base64.b64encode(f"{CLIENT_ID}:{CLIENT_SECRET}".encode()).decode()
    }
    data = {"grant_type": "client_credentials"}
    
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

SPOTIFY_ACCESS_TOKEN = get_spotify_token()


def get_artist_genre(artist_name):
    """Fetch the genre of an artist using Spotify API."""
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist&limit=1"
    headers = {"Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if "artists" in data and data["artists"]["items"]:
            return data["artists"]["items"][0]["genres"]  # Returns a list of genres
    return "Genre not found"
    
spotify_genre_data = []
   
for entry in spotify_data:
    ts = entry.get("ts", "Unknown Date")
    track_name = entry.get("master_metadata_track_name", "Unknown Track")
    artist_name = entry.get("master_metadata_album_artist_name", "Unknown Artist")
    track_uri = entry.get("spotify_track_uri", "Unknown URI")

    # Fetch genre using artist name
    genre = get_artist_genre(artist_name)

    spotify_genre_data.append({
        "timestamp": ts,
        "track": track_name,
        "artist": artist_name,
        "genre": genre,
        "spotify_track_uri": track_uri
    })
    
    time.sleep(1)  # Avoid hitting API rate limits

# Convert to DataFrame and display
df = pd.DataFrame(spotify_genre_data)

# Save results to a CSV file
df.to_csv("spotify_genre_data.csv", index=False)

print("Spotify Genre Data saved to 'spotify_genre_data.csv'")

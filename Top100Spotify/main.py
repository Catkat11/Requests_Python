from bs4 import BeautifulSoup  # Library for web scraping
import requests  # Library for making HTTP requests
import spotipy  # Spotify API library
from spotipy.oauth2 import SpotifyOAuth  # Library for Spotify OAuth authentication

# Spotify API credentials
SPOTIFY_CLIENT_ID = "ID"
SPOTIFY_CLIENT_SECRET = "SECRET"

# Prompt user to input the year they want to travel to
date = input("Which year do you want to travel to? Type this date in this format YYYY-MM-DD:")

# Get the Billboard Hot 100 chart for the specified date
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract song names from the parsed HTML
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
print(song_names)

# Authenticate with Spotify using OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               )
                     )

# Get the user's Spotify ID
user_id = sp.current_user()["id"]
print(user_id)

# Search for each song on Spotify and get its URI
song_uris = []
year = date.split("-")[0]  # Extract the year from the date
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]  # Get the URI of the first search result
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.")

# Create a new playlist on the user's Spotify account
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Bilboard 100", public=False)
print(playlist)

# Add the songs to the newly created playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

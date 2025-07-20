import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv

load_dotenv()

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

url = "https://www.billboard.com/charts/hot-100/"+date
header = {"User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
}
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
song_names_h3= soup.select("li ul li h3")

song_names = [song.getText().strip() for song in song_names_h3]


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
USERNAME = os.getenv("USERNAME")

scope = "playlist-modify-private playlist-modify-public"
authorization_object= SpotifyOAuth(scope=scope,
                                               redirect_uri=REDIRECT_URI,
                                               client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               show_dialog=True,
                                               username="Aasthayuli")

access_token = authorization_object.get_access_token(as_dict=False)
sp = spotipy.Spotify(auth_manager=authorization_object)
user_id = sp.current_user()["id"]


# Creates the new playlist
#
# CREATE_PLAYLIST_URL = f"https://api.spotify.com/v1/users/{user_id}/playlists"
# headers = {
#     "Authorization": f"Bearer {access_token}",
#     "Content-Type": "application/json"
# }
# data = {
#     "name": "top 100 songs from 24 may,2002",
#     "description": "added songs using python code",
#     "public": False
# }
# response = requests.post(url=CREATE_PLAYLIST_URL, headers=headers, data=json.dumps(data))
# print(response.status_code)
# print(response.json())  # This prints the created playlist details


# adding items to the playlist
playlist_id = "2VunKaZ1xGyvupzOmjzdpe"
# Got by right-click on the playlist name and then followed the code after "playlist/" in the url and removed the ? part

uris = []
for song in song_names:
    track_info = sp.search(q=song, type="track")
    try:
        uri = track_info["tracks"]["items"][0]["uri"]
        uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

data = {
    "uris": uris,
    "position":0
}
ADD_SONGS_URL= f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

response = requests.post(url=ADD_SONGS_URL, headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.json())
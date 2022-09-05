from webscrape import WebScrape
from spotify import SpotPlaylist

date = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD: ")
print("Grabbing Data from Billboard of that Date.")
webscrape = WebScrape(date)
spotipy = SpotPlaylist()
print("Searching to see if songs exist on Spotify")
song_uri_list = []

for i in range(0, len(webscrape.top_100)):
    artist = webscrape.artist[i]
    song = webscrape.top_100[i]
    song_uri_list.append(spotipy.song_list_creation(song_name=song, artist=artist))

playlist_id = spotipy.playlist_generation(date)
print("Adding songs to Playlist")

for songs in song_uri_list:
    spotipy.adding_songs(playlist_id=playlist_id, tracks=songs)

print(f"Completed! Enjoy your playlist https://open.spotify.com/playlist/{playlist_id}")

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import cred
import urllib.request
from PIL import Image


def main():
    auth_manager = SpotifyClientCredentials(client_id="ddad18f0d51242c8aa54f0ccb23b1ac7", client_secret="1cbf1c9f774f48e2916d61cc26776392")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID,
                                                   client_secret= cred.client_SECRET,
                                                   redirect_uri=cred.redirect_url))

    # artist_info(sp, 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu')
    user_playlists(sp)



# print("Add to queue result: " + sp.add_to_queue(uri="spotify:track:5uICWmZTLkpEVbK22PBP6e"))
# 'spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
def artist_info(sp, uri):
    # pulling up the artist, weezer, and printing out some information about them
    artist = sp.artist(uri)

    print(str(artist.keys()))

    print("Artist name: " + artist['name'])

    print("Artist genres: " + str(artist['genres']))
    # urllib.request.urlretrieve(artist['images'][0]['url'], artist['name'] + "0")
    # img = Image.open(artist['name'] + "0")
    # img.show()
    print("Artist images: " + artist['images'][0]['url'])

    # printing out the number of followers
    print("number of followers: " + str(artist['followers']['total']))

#printing out all of the user's playlists
def user_playlists(sp):
    playlists = sp.user_playlists('spotify')
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None


# playing all recently played songs
def recently_played_songs(sp):
    results = sp.current_user_recently_played()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

main()
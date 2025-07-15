import spotipy
from spotipy.oauth2 import SpotifyOAuth

username = 'your username here'
clientID = 'your id here'
clientSecret = 'your key here'
redirect_uri = 'http://localhost:1121'

def spotify_authenicate(client_id, client_secret, redirect_uri, username):
    scope = "user-read-currently-playing user-read-playback-state user-modify-playback-state playlist-read-private user-library-read"
    auth_manager = SpotifyOAuth(client_id, client_secret, redirect_uri, scope=scope, username=username)
    return spotipy.Spotify(auth_manager = auth_manager)

spotify = spotify_authenicate(client_id=clientID, client_secret=clientSecret, redirect_uri=redirect_uri, username=username)

def get_current_playing_info():
    global spotify
    current_track = spotify.current_user_playing_track()
    if current_track is None:
        return None
    
    artist_name = current_track['item']['artists'][0]['name']
    album_name = current_track['item']['album']['name']
    track_title = current_track['item']['name']

    return {
        "artist": artist_name,
        "album": album_name,
        "title": track_title
    }


def addtoque(query):
    global spotify
    uri = None
    spotsearch =spotify.search(q=query, limit=1, type="track")
    if spotsearch:
        uri = spotsearch['tracks']['items'][0]['uri']
        if uri:
            spotify.add_to_queue(uri)
        else:
                print("Error: No URI")
    else:
        print("Error: spotify search failed")


def playrequest(query, types):
    global spotify
    uri = None
    state = spotify.current_playback()
    if state:
        pass
    else:
        spotify.start_playback()
    if types == "track":
        spotsearch =spotify.search(q=query, limit=1, type=types)
        if spotsearch:
            uri = spotsearch['tracks']['items'][0]['uri']
            if uri:
                spotify.start_playback(uris=[uri])
            else:
                print("Error: No URI")
        else:
            print("Error: spotify search failed")
    elif types == "artist":
        spotsearch =spotify.search(q=query, limit=1, type=types)
        if spotsearch:
            uri = spotsearch['artists']['items'][0]['uri']
            if uri:
                spotify.start_playback(context_uri=uri)
            else:
                print("Error: No URI")
        else:
            print("Error: spotify search failed")
    elif types == "album":
        spotsearch =spotify.search(q=query, limit=1, type=types)
        if spotsearch:
            uri = spotsearch['albums']['items'][0]['uri']
            if uri:            
                spotify.start_playback(context_uri=uri)
            else:
                print("Error: No URI")
        else:
            print("Error: spotify search failed")
    elif types == "playlist":
        spotsearch =spotify.search(q=query, limit=1, type=types)
        if spotsearch:
            uri = spotsearch['playlists']['items'][0]['uri']
            if uri:
                spotify.start_playback(context_uri=uri)
            else:
                print("Error: No URI")
        else:
            print("Error: spotify search failed")
    else:
        print("Error: Invalid type")


def start_music():
    global spotify    
    try:
        spotify.start_playback()
    except spotipy.SpotifyException as e:
        return f"Error in starting playback: {str(e)}"
    
def stop_music():
    global spotify
    try:
        spotify.pause_playback()
    except spotipy.SpotifyException as e:
        return f"Error in starting playback: {str(e)}"
    
def skip_to_next():
    global spotify
    try:
        spotify.next_track()
    except spotipy.SpotifyException as e:
        return f"Error in starting playback: {str(e)}"
    
def skip_to_previous():
    global spotify
    try:
        spotify.previous_track()
    except spotipy.SpotifyException as e:
        return f"Error in starting playback: {str(e)}"
    

def getspotplaystate():
    state = None
    state = spotify.current_playback()
    if state:
        return state
    else:
        print('shit')


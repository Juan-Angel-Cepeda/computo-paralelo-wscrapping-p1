import threading
import lyricsgenius as lg
from lyricsgenius import OAuth2

#GENIUS_TOKEN = "hbbR2NA8_o-1InmVM4KUcCfKtLRGcOyRqkL9waVpFHzJVs_6lWMcxuqLdntDAbaX"
#genius = lg.Genius(GENIUS_TOKEN)
client_id = "Lw1hYZTi0GwpPegSqsSW7b-zT1nf-xLSrnNAVp3cBR-_cgNC2A9hZy44qF6uhZup"
redirect_uri = "threading-lyrics"
auth = OAuth2.client_only_app(
    client_id,
    redirect_uri,
    scope='all'
)
token = auth.prompt_user()
genius = lg.Genius(token)

def go_for_my_lyrics(title):
    lyrics = []
    songs = genius.search_songs(title)
    for song in songs['hits']:
        url = song['result']['url']
        song_lyrics = genius.lyrics(song_url = url)
        lyrics.append(song_lyrics)
    return lyrics



def call_lyrics(titles):
    threads = [threading.Thread(target=go_for_my_lyrics, args=(title,)) for title in titles]
    for thread in threads:
        thread.start()
    
    my_lyrics = []
    for thread in threads:
        my_lyrics.append(thread.join())
    
    return my_lyrics
import threading
import lyricsgenius as lg

GENIUS_TOKEN = "hbbR2NA8_o-1InmVM4KUcCfKtLRGcOyRqkL9waVpFHzJVs_6lWMcxuqLdntDAbaX"
genius = lg.Genius(GENIUS_TOKEN)

def go_for_my_lyrics(title):
    artist = genius.search_artist(title, max_songs=1, sort="title")
    return artist.songs



def call_lyrics(titles):
    threads = [threading.Thread(target=go_for_my_lyrics, args=(title,)) for title in titles]
    for thread in threads:
        thread.start()
    
    my_lyrics = []
    for thread in threads:
        my_lyrics.append(thread.join())
    
    return my_lyrics
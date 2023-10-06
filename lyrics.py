import threading
import lyricsgenius as lg

GENIUS_TOKEN = "hbbR2NA8_o-1InmVM4KUcCfKtLRGcOyRqkL9waVpFHzJVs_6lWMcxuqLdntDAbaX"
genius = lg.Genius(GENIUS_TOKEN)

#API_GOOGLE_KEY = st.secrets["API_GOOGLE_KEY"]
#ENGINE_ID = st.secrets["ENGINE_ID"]

#extract_lyrics = SongLyrics(API_GOOGLE_KEY, ENGINE_ID)

def go_for_my_lyrics(title):
    song = genius.search_song(title=title)
    lyrics = song.lyrics
    return lyrics


def call_lyrics(songs):
    threads = [threading.Thread(target=go_for_my_lyrics, args=(song,)) for song in songs]
    for song in threads:
        song.start()
    
    my_lyrics = []
    for thread in threads:
        my_lyrics.append(thread.join())
    
    return my_lyrics
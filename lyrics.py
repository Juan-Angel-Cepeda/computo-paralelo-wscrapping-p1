from lyrics_extractor import SongLyrics
import threading
import streamlit as st


API_GOOGLE_KEY = st.secrets["API_GOOGLE_KEY"]
ENGINE_ID = st.secrets["ENGINE_ID"]

extract_lyrics = SongLyrics(API_GOOGLE_KEY, ENGINE_ID)

def go_for_my_lyrics(song):
    
    lyrics = extract_lyrics.get_lyrics(song)
        #lyrics = "Lyrics not found"
    return lyrics

def call_lyrics(songs):
    threads = [threading.Thread(target=go_for_my_lyrics, args=(song,)) for song in songs]
    for song in threads:
        song.start()
    
    my_lyrics = []
    for thread in threads:
        my_lyrics.append(thread.join())
    
    return my_lyrics
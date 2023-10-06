import streamlit as st
import lyrics as ly

st.title("Get your Lyrics")
new_song = st.markdown('''## :red[Add your songs]''')
song = st.text_input(label="Add your song",label_visibility="hidden")
add_song = st.button("Add my song")

if 'songs' not in st.session_state:
    st.session_state.songs = []

if add_song:
    st.session_state.songs.append(song)

st.markdown("## :green[Your songs]")
for song in st.session_state.songs:
    st.markdown(f"### {song}")
    st.divider()

if st.button("Get my lyirics"):
    lyrics_songs = ly.call_lyrics(st.session_state.songs)
    for lyric in lyrics_songs:
        st.markdown(f"### :blue[{lyric}]")
        st.divider()


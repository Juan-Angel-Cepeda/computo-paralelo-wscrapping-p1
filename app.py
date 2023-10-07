import streamlit as st
import pokedex as pkdx

st.title("Welocme to pokeScrapper")
new_pokemon = st.markdown('''## :red[Add the pokemons you want to know about]''')
pokemon = st.text_input(label="Add your pokemon",label_visibility="hidden")
add_pokemon = st.button("Go to pokedex")

if 'pokemons' not in st.session_state:
    st.session_state.pokemons = []

if add_pokemon:
    st.session_state.pokemons.append(pokemon)

st.markdown("## :green[Your pokemons]")
for pokemon in st.session_state.pokemons:
    st.markdown(f"### {pokemon}")
    st.divider()

if st.button("Get my pokemons"):
    pokeinfo = pkdx.run_pokedex(st.session_state.pokemons)
    num_pokemons = len(pokeinfo)
    cols = st.columns(3)
    
    for i, (pokemon, info) in enumerate(pokeinfo.items()):
        name, image, type = info
        cols[i % 3].markdown(f"### {name}")
        cols[i % 3].image(image, caption=f"Image of {name}", use_column_width=True)
        cols[i % 3].markdown(f"### Type: {type}")
        cols[i % 3].divider()


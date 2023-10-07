import streamlit as st
import pokedex as pkdx

st.title("Welocme to pokeScrapper")
new_pokemon = st.markdown('''## :red[Add the pokemons you want to know about]''')
pokemon = st.text_input(label="Add your pokemon",label_visibility="hidden")
add_pokemon = st.button("Go to pokedex")
pokeball = "./img/pokebola.png"

if 'pokemons' not in st.session_state:
    st.session_state.pokemons = []

if add_pokemon:
    st.session_state.pokemons.append(pokemon)

st.markdown("## :green[Your pokemons]")
for pokemon in st.session_state.pokemons:
    st.image(pokeball, caption=pokemon, width=100)
    st.divider()

if st.button("Get my pokemons"):
    pokeinfo = pkdx.run_pokedex(st.session_state.pokemons)
    num_pokemons = len(pokeinfo)
    cols = st.columns(1)
    for pokemon, info in enumerate(pokeinfo.items()):
        name, image, type, abilities = info
        fig = pkdx.draw_stats(abilities)
        cols[0].markdown(f"### {name}")
        cols[0].image(image, caption=f"Image of {name}", use_column_width=True)
        cols[0].markdown(f"### {type}")
        cols[0].markdown(f"### Abilities")
        cols[0].pyplot(fig)
        cols[0].divider()

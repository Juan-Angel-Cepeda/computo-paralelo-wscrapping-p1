from bs4 import BeautifulSoup
import requests
import threading


def request(pokemon,pokedict,lock):
    url = f'https://www.pokemondb.net/pokedex/{pokemon}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        name = soup.find('title').text.split(' Pokédex')[0]
        image = soup.find('meta',property='og:image')['content']
        type = soup.find('a', class_='type-icon').text
        #ability = soup.find('div', class_='column-7').text.strip()
        pokeinfo = [name, image, type]
        with lock:
            pokedict[pokemon] = pokeinfo    
        return 
    else:
        print(f'Error al obtener el código {response.status_code}')
        return
    
def run_pokedex(pokemons):
    threads = []
    pokedict = {}
    lock = threading.Lock()
    
    for pokemon in pokemons:
        threads.append(threading.Thread(target=request, args=(pokemon,pokedict,lock)))
    
    for thread in threads:
        thread.start()
        
    for thread in threads:
        thread.join()
        
    return pokedict
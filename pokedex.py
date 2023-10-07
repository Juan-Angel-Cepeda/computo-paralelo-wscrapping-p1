from bs4 import BeautifulSoup
import requests
import threading
import matplotlib.pyplot as plt
import numpy as np


def request(pokemon,pokedict,lock):
    url = f'https://www.pokemondb.net/pokedex/{pokemon}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        name = soup.find('title').text.split(' Pokédex')[0]
        image = soup.find('meta',property='og:image')['content']
        type = soup.find('a', class_='type-icon').text
        abilities = {}
        vitals_tables = soup.find_all('table', class_='vitals-table',)
        abilities_table = vitals_tables[3]
        print(abilities_table)
        for row in abilities_table.find_all('tr'):
            th = row.find('th')
            td = row.find('td',class_='cell-num')
            if th and td:
                abilities[th.text.strip()] = td.text.strip()
            
        pokeinfo = [name, image, type,abilities]
        
        with lock:
            pokedict[pokemon] = pokeinfo    
        
        return 
    else:
        print(f'Error al obtener el código {response.status_code}')
        return

def draw_stats(abilities):
    abilities = abilities.copy()
    abilities.pop('Total',None)
    stats = list(abilities.keys())
    values = [int(val) for val in abilities.values()]
    values += values[:1]
    num_stats = len(stats)
    
    angles = np.linspace(0, 2*np.pi,num_stats, endpoint=False).tolist()
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6,6),subplot_kw={'polar':True})
    ax.fill(angles,values,color="blue",alpha=0.25)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(stats)
    
    for angle, value, stat in zip(angles,values,stats):
        ax.text(angle,value, str(value),color="black")
    
    return fig
            
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

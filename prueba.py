import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_animes = []
for i in range(0,150,50):
    lista = []
    my_anime_url = requests.get(f'https://myanimelist.net/topanime.php?limit={i}')
    lista.append(my_anime_url)

    for animelt in lista:
        s = BeautifulSoup(animelt.text,'lxml')
        animes =s.find_all('div',attrs={'class':'detail'})
        
        for g in animes:
            lista_animes.append(g.h3.a.get('href'))
            print('link:',g.h3.a.get('href'))



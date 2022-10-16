from asyncio.log import logger
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
logging.basicConfig(level=logging.INFO)

lista_animes = []
for i in range(0,1000,50):
    lista = []
    my_anime_url = requests.get(f'https://myanimelist.net/topanime.php?limit={i}')
    lista.append(my_anime_url)

    for animelt in lista:
        s = BeautifulSoup(animelt.text,'lxml')
        animes =s.find_all('div',attrs={'class':'detail'})
        
        for g in animes:
            lista_animes.append(g.h3.a.get('href'))
            print('link:',g.h3.a.get('href'))



def obtener_info(s_anime):
    animes_dic = {}

    # Extraer el titulo
    titulo = s_anime.find('h1',attrs={'class':'title-name h1_bold_none'})
    if titulo:
        animes_dic["titulo"]=titulo.text
    else:
        animes_dic['titulo']=None
     # Extraer el Synopsis
    Synopsis = s_anime.find('p',attrs={'itemprop':'description'})
    if Synopsis:
        animes_dic["Synopsis"]=Synopsis.text
    else:
        animes_dic['Synopsis']=None
    # Extraer el imagen
    media = s_anime.find('div',attrs={'id':'content'})
    img =media.a.img.get('data-src')
    if img:
        animes_dic["img"]=img
    else:
        animes_dic['img']=None

    return animes_dic


def scrap_nota(url):
    try:
        un_anime = requests.get(url)
    except Exception as e:
        print('Error Scrapeando URL',url)
        print(e)
        print('\n')
    if un_anime.status_code != 200:
         print(f'Error obteniendo Anime {url}')
         print(f'status Code = {un_anime.status_code}')
         return None
    s_anime = BeautifulSoup(un_anime.text,'lxml')

    ret_dict = obtener_info(s_anime)
    ret_dict['url']=url

    return ret_dict

def extract():
    data = []
    for i,anime in enumerate(lista_animes):
        logger.info(f' {i}/{len(lista_animes)}... Scrapeando {anime}')
        data.append(scrap_nota(anime))

    df = pd.DataFrame(data)


    df.to_csv("Animes MyAnimeList.csv")
        
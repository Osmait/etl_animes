import requests
from bs4 import BeautifulSoup
import pandas as pd

my_anime_list = requests.get('https://myanimelist.net/topanime.php')
s = BeautifulSoup(my_anime_list.text,'lxml')
animes =s.find_all('div',attrs={'class':'detail'})
anime =animes[0]
anime.h3.a.get_text()
anime.h3.a.get('href')
lista_animes= [anime.h3.a.get('href') for anime in animes ]



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
        print(f'Scrapeando anime {i}/{len(lista_animes)}...')
        data.append(scrap_nota(anime))

    df = pd.DataFrame(data)


    df.to_csv("Animes MyAnimeList.csv")
        
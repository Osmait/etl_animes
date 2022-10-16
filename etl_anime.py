from asyncio.log import logger
from email.mime import base
from animes_model import Anime
from base import Base,Engine,Session
import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd


class AnimeList:

    def read(self):
        df_animes = pd.read_csv('/home/osmait/Documentos/Work-space/python/etl/etl_animes/Animes MyAnimeList.csv')

        return df_animes

    def transform(self,df_animes):
            df_animes.drop(['Unnamed: 0'],axis=1,inplace=True)
            df_animes['id']= range(1,len(df_animes)+1)

            return df_animes
        

    
    def load(self,df_animes):
        Base.metadata.create_all(Engine)
        session = Session()

        for i, r in df_animes.iterrows():
            logger.info('Loading {} in DataBase'.format (r['titulo']))
            anime = Anime(r['id'],r['titulo'],r['Synopsis'],r['img'],r['url'])
            session.add(anime)
            session.commit()
            session.close()



def etl():
    anime_list = AnimeList()
    read = anime_list.read()
    transfrom = anime_list.transform(read)
    return anime_list.load(transfrom)

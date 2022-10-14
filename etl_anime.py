
import sqlalchemy 
import pandas as pd


class AnimeList:

    def read(self):
        df_animes = pd.read_csv('/home/osmait/Documentos/Work-space/python/etl/Animes MyAnimeList.csv')
        return df_animes

    def transform(self,df_animes):
            df_animes.drop(['Unnamed: 0'],axis=1,inplace=True)
            df_animes.index.rename(name="id",inplace=True)
            return df_animes
        

    
    def load(self,df_animes):
        engine =sqlalchemy.create_engine('sqlite:///animes')
        df_animes.to_sql('Animes',engine)



def etl():
    anime_list = AnimeList()
    read = anime_list.read()
    transfrom = anime_list.transform(read)
    return anime_list.load(transfrom)

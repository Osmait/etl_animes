from email.mime import base
from sqlalchemy import String,Column,Integer
from base import Base




class Anime(Base):


    __tablename__ = 'anime'
    id = Column(Integer,primary_key = True)
    title = Column(String)
    synopsis =  Column(String)
    img =  Column(String)
    url =  Column(String)


    def __init__(self,id,title,synopsis,img,url):
        self.id = id
        self.title = title
        self.synopsis = synopsis
        self.img = img
        self.url = url
                


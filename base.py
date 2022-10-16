from email.mime import base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from decouple import config





Engine = create_engine(config('URL_DB'))
Session = sessionmaker(bind=Engine)

Base = declarative_base()
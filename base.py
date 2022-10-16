from email.mime import base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker





Engine = create_engine("postgresql://osmait:123456@localhost:5432/animes")
Session = sessionmaker(bind=Engine)

Base = declarative_base()
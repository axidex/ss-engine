import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'

    client = Column(Integer, primary_key=True)
    subject_name = Column(String)

    load_dttm = Column(DateTime, default=datetime.datetime.now())
from database import Base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

class SurfSpot(Base):
    __tablename__='spots'
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    sec_name = Column(String)
    lat = Column(Integer)
    long = Column(Integer)

class Session(Base):
    __tablename__='sessions'
    id = Column(Integer,primary_key=True, index=True)
    spot_id = Column(Integer)
    date = Column(String)
    strength = Column(Integer)
    clean = Column(Integer)
    overal = Column(Integer)
    swellHeight = Column(Float)
    windSpeed = Column(Float)
    windDirection = Column(Float)
    description = Column(String)
    seaLevel = Column(Float)
    secondarySwellDirection = Column(Float)
    secondarySwellHeight = Column(Float)
    secondarySwellPeriod = Column(Float)
    swellDirection = Column(Float)
    swellPeriod = Column(Float)
    waveDirection = Column(Float)
    waveHeight = Column(Float)
    windDirection = Column(Float)
    windSpeed = Column(Float)
    windWaveDirection = Column(Float)
    windWaveHeight = Column(Float)
    windWavePeriod = Column(Float)

class Users(Base):
    __tablename__="users"
    id = Column(Integer,primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    api_key = Column(String)


    




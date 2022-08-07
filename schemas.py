
from pydantic import BaseModel
from typing import Dict, List, Union



class Spots(BaseModel):
    class Config():
        orm_mode = True

class Forcast(BaseModel):
    date = str
    strength = int
    clean = int
    overal = int
    waveHeight = float
    swellHeight = float
    wind = float
    direction = float
    description = str
    seaLevel = float
    secondarySwellDirection = float
    secondarySwellHeight = float
    secondarySwellPeriod = float
    swellDirection = float
    swellHeight = float
    swellPeriod = float
    time = str
    waveDirection = float
    waveHeight = float
    windDirection = float
    windSpeed = float
    windWaveDirection = float
    windWaveHeight = float
    windWavePeriod = float

class Sessions(BaseModel):
    spot_id: int
    forcast:  Union[Forcast, None] = None



class SurfSpot(BaseModel):
    name: str
    # location: list[float, float]
    # secondname: str
    # sessions: Sessions
    

class ShowSpots(BaseModel):
    # spots: {"id" = id, "name"=name}
    spot : str
    

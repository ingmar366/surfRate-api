import json5
from sqlalchemy.orm import Session
from fastapi import status
import models


def create_session(spot_id,forcast,db:Session):
    dataDict = json5.loads(forcast) 
    # print(type(dataDict["forcast"][0]["secondarySwellDirection"]["sg"]))
    if(len(dataDict)>0):
        new_session = models.Session(spot_id = spot_id, date=dataDict["time"],strength = dataDict["strength"], clean=dataDict["clean"], overal=dataDict["overal"],swellHeight=dataDict["swellHeight"]["sg"],description=dataDict["description"],seaLevel = dataDict["seaLevel"]["sg"],secondarySwellDirection=dataDict["secondarySwellDirection"]["sg"],secondarySwellHeight = dataDict["secondarySwellHeight"]["sg"],secondarySwellPeriod = dataDict["secondarySwellPeriod"]["sg"],
        swellDirection = dataDict["swellDirection"]["sg"],
        swellPeriod = dataDict["swellPeriod"]["sg"],
        waveDirection = dataDict["waveDirection"]["sg"],
        waveHeight = dataDict["waveHeight"]["sg"],
        windDirection = dataDict["windDirection"]["sg"],
        windSpeed = dataDict["windSpeed"]["sg"],
        windWaveDirection = dataDict["windWaveDirection"]["sg"],
        windWaveHeight = dataDict["windWaveHeight"]["sg"],
        windWavePeriod = dataDict["windWavePeriod"]["sg"])
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        return status.HTTP_201_CREATED
    return status.HTTP_204_NO_CONTENT
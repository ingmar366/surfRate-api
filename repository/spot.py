from fastapi import status
from sqlalchemy.orm import  Session
import models
import json5

# and spot_dict["location"][0] == float)
#  and spot_dict["secondName"]==str
def create_spot(data,db :Session):
    spot_dict = json5.loads(data)
    # print(type(spot_dict["name"]))
    if(isinstance(spot_dict["name"], str) and isinstance(spot_dict["secondName"], str) and isinstance(spot_dict["location"][0], float)):
        print(type(spot_dict["name"]))

        new_spot = models.SurfSpot(name=spot_dict["name"], sec_name=spot_dict["secondName"],lat=spot_dict["location"][0], long=spot_dict["location"][1])
        db.add(new_spot)
        db.commit()
        db.refresh(new_spot)
        return status.HTTP_201_CREATED
    return status.HTTP_400_BAD_REQUEST

def get_spots(db:Session):
    spots =  db.query(models.SurfSpot).all()
    spotASession = {}
    for spot in spots:
        sessions = db.query(models.Session).filter(spot.id == models.Session.spot_id).all()
        if(len(sessions) >0):
            print('working')
            spotASession.update({spot.id:{"spot":spot,"sessions":sessions}}) 
        else:spotASession.update({spot.id:{"spot":spot}})
    return spotASession
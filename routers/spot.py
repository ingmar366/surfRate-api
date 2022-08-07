from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import  Session
import database, models
import json5
from repository import spot

router = APIRouter(
    prefix="/spot", 
    tags=["Spot"]
)


@router.post('/create')
def create_spot(data,db :Session = Depends(database.get_db)):
    return spot.create_spot(data,db)


@router.get('/all')
def get_spots(db:Session = Depends(database.get_db)):
    return spot.get_spots(db)
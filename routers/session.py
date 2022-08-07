from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import  Session
import database
from repository import session

router = APIRouter(
    prefix="/session", 
    tags=["Session"]
)

@router.post('/create/{spot_id}', status_code=status.HTTP_201_CREATED)
def create_session(spot_id,forcast,db:Session = Depends(database.get_db)):
    return session.create_session(spot_id,forcast,db)



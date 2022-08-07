from fastapi import APIRouter, Depends,status
from sqlalchemy.orm import  Session
import database, models
from hashing import Hash
from repository import users

router = APIRouter(
    prefix="/user", 
    tags=["User"]
)

@router.post('/')
def create_user(data,db :Session = Depends(database.get_db)):
    return users.create_user(data,db)

@router.get('/login')
def login(username,password,db :Session = Depends(database.get_db)):
    return users.login(username,password,db)
    
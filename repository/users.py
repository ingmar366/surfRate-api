import json5, models
from sqlalchemy.orm import Session
from fastapi import status
from hashing import Hash



def create_user(data,db:Session):
    user_dict = json5.loads(data)
    print(user_dict)
    if(len(user_dict["apiKey"]) < 70 or type(user_dict["apiKey"])!= str):
        return status.HTTP_406_NOT_ACCEPTABLE
    same_username = db.query(models.Users).filter(user_dict["username"] == models.Users.username).first()
    if same_username != None:    
        return status.HTTP_409_CONFLICT
    new_user = models.Users(username=user_dict["username"],password=Hash.bcrypt(user_dict["password"]), api_key=user_dict["apiKey"])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return status.HTTP_201_CREATED

def login(username,password,db :Session):
    user = db.query(models.Users).filter(models.Users.username == username).first()
    if (Hash.verify(user.password,password)):
        return user.api_key
    return status.HTTP_406_NOT_ACCEPTABLE
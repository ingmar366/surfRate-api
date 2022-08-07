from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import  Session
import database,models, json5
from database import engine
from fastapi.middleware.cors import CORSMiddleware
from routers import user, spot, session



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

models.Base.metadata.create_all(engine)


app.include_router(user.router)
app.include_router(spot.router)
app.include_router(session.router)




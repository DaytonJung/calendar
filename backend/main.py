from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from db.session import SessionLocal, engine

#To start local route "uvicorn backend.main:app --reload"
#To view docs and redoc "{IP}/doc or {IP}/redoc"

app = FastAPI()

@app.get("/ping")
def read_ping():
    return {"message": "pong"}

get_db = SessionLocal

@app.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    # just a placeholder to confirm the connection works
    return {"message": "DB session is working"}
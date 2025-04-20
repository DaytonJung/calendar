from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from backend.db.session import get_db

#To start local route "uvicorn backend.main:app --reload"
#To view docs and redoc "{IP}/doc or {IP}/redoc"

app = FastAPI()


#Test routes
@app.get("/ping")
def read_ping():
    return {"message": "pong"}

@app.get("/ping-db")
def ping_db(db: Session = Depends(get_db)):
    # just a placeholder to confirm the connection works
    return {"message": "DB session is working"}
from fastapi import FastAPI
import uvicorn

#To start local route "uvicorn backend.main:app --reload"
#To view docs and redoc "{IP}/doc or {IP}/redoc"

app = FastAPI()

@app.get("/ping")
def read_ping():
    return {"message": "pong"}
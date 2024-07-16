from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from lib import get_data

load_dotenv()

app = FastAPI(title="Horoscope API", description="Horoscope data API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://divineconnection.co.in"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/horoscope", summary="horoscope")
async def read_items(horoscope_data: str, time: str):
    try:
        response = get_data(horoscope_data, time)
        if response:
            return {"response": response}
        else:
            raise HTTPException(status_code=404, detail="Horoscope data not fou>
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def index():
    return {"message": "Hello World use /docs for swagger docs"}

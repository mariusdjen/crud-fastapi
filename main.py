import os
import httpx
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List
from dotenv import load_dotenv

app = FastAPI()

# Environnement
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_ID = os.getenv("BASE_ID")
TABLE_NAME = os.getenv("TABLE_NAME")
AIRTABLE_URL = os.getenv("AIRTABLE_URL")

# En-têtes pour authentification
HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

# Schéma
class Client(BaseModel):
    firstName: str
    lastName: str
    country: str
    email: str
    phoneNumber: str

#clients = []

@app.get("/")
def read():
    return {"message": "Bienvenue bro !"}

        
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

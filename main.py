import httpx
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# Environnement
API_KEY = "patMHyyciHFQDXGbx.b0c9b6fb83321615704491e0936cfc70c948c0d75b9a0d2b90e38dc66368a9c4"
BASE_ID = "appXYtNOt5023G2HG"
TABLE_NAME = "Client"
AIRTABLE_URL = f'https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}'

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

@app.post("/create", response_model=Client)
async def create(client: Client):
    data = {
        "fields": {
            "firstName": client.firstName,
            "lastName": client.lastName,
            "country": client.country,
            "email": client.email,
            "phoneNumber": client.phoneNumber,
        }
    }

    async with httpx.AsyncClient() as http_client:
        try:
            # Envoi de la requête POST vers AirTable
            response = await http_client.post(AIRTABLE_URL, headers=HEADERS, json=data)
            response.raise_for_status()  # Vérifie si la requête a échoué
            # Retourner un message de succès avec le code 201
            return JSONResponse(
                status_code=201,
                content={"message": "Client créé avec succès"}
            )

        except httpx.RequestError as e:
            # Erreur lors de la requête
            return JSONResponse(
                status_code=400,
                content={"message": f"Erreur lors de la requête: {e}"}
            )
        except httpx.HTTPStatusError as e:
            # Erreur liée à l'HTTP
            return JSONResponse(
                status_code=response.status_code,
                content={"message": f"Erreur HTTP: {e}"}
            )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

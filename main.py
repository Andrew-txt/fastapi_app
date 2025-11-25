from fastapi import Body, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated
import uvicorn
import aiohttp
from utils import settings

from utils import generate_redirect_google_uri, get_user_account_data
import jwt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/auth/google/url")
def get_google_oauth_uri():
    uri = generate_redirect_google_uri()
    return RedirectResponse(uri, status_code=302)


@app.post("/auth/google/callback")
async def handle_code(
    code: Annotated[str, Body(embed=True)] # type: ignore
): 
    google_token_url = "https://oauth2.googleapis.com/token"
    async with aiohttp.ClientSession() as session:
        async with session.post(
            url=google_token_url,
            data={
                "client_id": settings.GOOGLE_CLIENT_ID,
                "client_secret": settings.GOOGLE_CLIENT_SECRET,
                "grant_type": "authorization_code",
                "redirect_uri": "http://localhost:3000/auth/google",
                "code": code,
            }
        ) as response:
            res = await response.json()
            id_token = res["id_token"]
            
            return get_user_account_data(token=id_token)
        



@app.get("/auth/check")
async def check_user_auth():
    ...
import urllib.parse
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv
import jwt
from typing import Optional
from psycopg2 import sql
from db import add_user_data_to_db, conn

# from db import add_data_to_db, curs


# сгенерирует редиректный юрл и вернет его / работает
def generate_redirect_google_uri():
    query_params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": "http://localhost:3000/auth/google",
        "response_type": "code",
        "scope": " ".join([
            "openid",
            "email",
            "profile"
        ]),
        "access_type": "offline",
        # state 
    }
    query_str = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    return f"{base_url}?{query_str}"


class Settings(BaseSettings):
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    DB_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env") 


# здесь получим данные пользователя нужные нам и упакуем в словарь/ работает
def get_user_account_data(token):
    given_data = jwt.decode(
    token,
    algorithms=["RS256"],options={"verify_signature": False}
    )
    
    user_data = {
        "email": given_data["email"],
        "name": given_data["name"],
        "picture": given_data["picture"]
    }
    add_user_data_to_db(conn, user_data)
    return user_data


settings = Settings()







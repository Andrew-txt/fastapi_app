import urllib.parse
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


class Settings(BaseSettings):
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    model_config = SettingsConfigDict(env_file=".env") 


def generate_redirect_google_uri():
    query_params = {
        "client_id": settings.GOOGLE_CLIENT_ID,
        "redirect_uri": "http://localhost:4000/auth/google",
        "response_type": "code",
        "scope": " ".join([
            "openid",
            "email",
            "profile"
        ]),
        "access_type": "offline",
        # state потом
    }
    query_str = urllib.parse.urlencode(query_params, quote_via=urllib.parse.quote)
    base_url = "https://accounts.google.com/o/oauth2/v2/auth"
    return f"{base_url}?{query_str}"

settings = Settings()

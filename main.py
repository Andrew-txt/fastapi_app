from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from oauth_google import generate_redirect_google_uri

app = FastAPI()

@app.get("/auth/google/url")
def get_google_oauth_uri():
    uri = generate_redirect_google_uri()
    return RedirectResponse(uri, status_code=302)

# if __name__ == "__main__":
#     uvicorn.run(
#         "main:app",
#         host="127.0.0.1",
#         port=8000,
#         reload=True, 
#         log_level="info"
#     )

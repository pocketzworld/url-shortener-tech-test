from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.responses import Response
from pydantic import BaseModel
from redisstore import RedisStore
import encoder
from utils import fix_protocol

app = FastAPI()
BASE_URL: str = "http://locahost:8000"
urlstore = RedisStore()


class ShortenRequest(BaseModel):
    url: str

@app.post("/url/shorten")
async def url_shorten(request: ShortenRequest):
    """
    Given a URL, generate a short version of the URL that can be later resolved to the originally
    specified URL.
    """
    url = request.url

    inserted_id = urlstore.insert(url)
    short_url = encoder.encode(inserted_id)
    return {"short_url": f"{BASE_URL}/r/{short_url}"}
    
class ResolveRequest(BaseModel):
    short_url: str


@app.get("/r/{short_url}")
async def url_resolve(short_url: str):
    """
    Return a redirect response for a valid shortened URL string.
    If the short URL is unknown, return an HTTP 404 response.
    """
    id = encoder.decode(short_url)
    url = urlstore.get(id)
    if not url:
        message = f"no record found for '{short_url}'"
        return Response(message, 404)
    url = fix_protocol(url)
    return RedirectResponse(url)


@app.get("/")
async def index():
    return "Your URL Shortener is running!"


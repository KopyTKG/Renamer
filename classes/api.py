import requests, os, json
from dotenv import load_dotenv

load_dotenv()

def FetchMovie(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("Auth")
    }
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)
    return response

def FetchVideos(id):
    url = f"https://api.themoviedb.org/3/movie/{id}/videos?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("Auth")
    }
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)
    return response

def FetchArtwork(id):
    url = f"https://api.themoviedb.org/3/movie/{id}/images"
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("Auth")
    }
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)
    return response


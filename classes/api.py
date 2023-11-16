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
    parsed = ParseVideosToArray(response)
    return parsed


def ParseVideosToArray(response):
    videos = []
    for video in response["results"]:
        parsedVideo = {
            "key": video["key"],
            "type": video["type"],
            "name": video["name"],
            "published_at": video["published_at"]
        }
        videos.append(parsedVideo)
    return videos
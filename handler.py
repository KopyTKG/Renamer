import requests, os, json, csv
from dotenv import load_dotenv
from pymongo import MongoClient
from datetime import datetime
from Renamer import LoadMovies

load_dotenv()

def DB(collectioName="Movie"):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = os.getenv("CONNECTION_STRING")
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   dbname = client["MongoMovieDB"]
   collection = dbname[collectioName]
   return collection
 

def HandleAPI(id):
    url = f"https://api.themoviedb.org/3/movie/{id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": os.getenv("Auth")
    }
    response = requests.get(url, headers=headers)
    response = json.loads(response.text)
    return response



def Parser(movie, response):
    overview = ""
    poster = ""
    backdrop = ""
    vote = 0
    tagline = ""

    try:
        overview = response["Overview"]
        poster = response["Poster_path"]
        backdrop = response["Backdrop_path"]
        vote = response["Vote_average"]
        tagline = response["Tagline"]
    except:
        overview = response["overview"]    
        poster = response["poster_path"]
        backdrop = response["backdrop_path"]
        vote = response["vote_average"]
        tagline = response["tagline"]
    
    geners = []

    for genre in response["genres"]:
        geners.append(genre["id"])

    return {
        "_id": movie["id"],
        "imdb_id": response["imdb_id"],
        "title": movie["title"],
        "year": movie["year"],
        "quality": movie["quality"],
        "description": overview,
        "backdrops": [
            {
                'src': backdrop,
            }
        ],
        "posters": [
            {
                'src': poster,
            }
        ], 
        "rating": vote,
        "tagline": tagline,
        "genres": geners,
        "createdAt": datetime.fromtimestamp(os.stat(f"../Movies/{movie['title']} ({movie['year']}) [{movie['quality']}] #{movie['id']}").st_ctime),
        "updatedAt": datetime.now()

    }

def Inject(object, db):
    try:
        db.insert_one(object)
    except:
        pass
    
def MainCycle(movies):
    collection = DB()
    for movie in movies:
        response = HandleAPI(movie["id"])
        movie = Parser(movie, response)
        Inject(movie, collection)

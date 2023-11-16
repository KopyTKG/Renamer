from datetime import datetime
import os


def Parser(movie, response, videos):
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
    
    genres = []

    for genre in response["genres"]:
        genres.append(genre["name"])

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
        'language': movie["language"],
        "rating": vote,
        "tagline": tagline,
        "genres": genres,
        "videos": videos,
        "createdAt": datetime.fromtimestamp(os.stat(f"../Movies/{movie['title']} ({movie['year']}) [{movie['quality']}] #{movie['id']} <{movie['language']}>").st_ctime),
        "updatedAt": datetime.now()

    }
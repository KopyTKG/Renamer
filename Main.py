import os
from typing import Any

# classes
from classes.queue import *
from classes.file import *
from classes.db import *
from classes.progress import *
from classes.api import *
from classes.parser import *


os.system("./MoviesGrep.sh")

Locations = {
    "left": "left.txt",
    "output": "./Dump/output.txt",
    "movies": "./Dump/movies.txt",
    "csv": "./Out/movies.csv",
    "base": "../Movies"
}


class Movie():
    def __init__(self, title: str, year: int, quality: str, language: str):
        self._title = title
        self._year = year
        self._quality = quality
        self._id = 0
        self._language = language
    
    def setId(self, id: int):
        self._id = id
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new_title):
        self._title = new_title
    def __str__(self):
        return f"{self._id},'{self._title}',{self._year},'{self._quality}','{self._language}'"


def addToClipBoard(text):
    command = f'echo \"{text.strip()}\" | xclip -selection clipboard'
    os.system(command)

def getData(data: str):
    title = (data.split("(")[0]).strip()
    year = data.split("(")[1].split(")")[0]
    quality = data.split("[")[1].split("]")[0] 
    try:
        language = data.split("<")[1].split(">")[0]
    except:
        language = "en-US"

    movie = Movie(title, year, quality, language)
    try:
        ide = (data.split('#')[1]).split(" ")[0]
        movie.setId(ide)
    except:
        ...

    return movie


def Main():
    left = Queue()
    setId = True

    # Creating output file if it doesn't exist
    if not os.path.exists(Locations["output"]):
        with open(Locations["output"], "w") as f:
            pass

    # Creating left file if it doesn't exist        ide = movie[0].replace("'", "")

    # File is used to keep memory of untagged movies
    if not os.path.exists(Locations["left"]):
        with open(Locations["movies"], "r") as f:
            lines = f.read()
            left.set(lines.split("\n"))
            with open(Locations["left"], "w") as w:
                for line in left:
                    w.write(line + "\n")
    else:
        with open(Locations["left"], "r") as f:
            lines = f.read()
            splitted = lines.split("\n")
            if len(splitted) > 1:
                left.set(splitted)
            else:
                setId = False
                print("No movies found")

    if setId:
        movies = Queue()
        for _ in range(len(left)):
            line = left.pop()
            if line == "":
                continue
            if "#" not in line:
                print("No id found")
                movie = getData(line)
                addToClipBoard(movie.title)
                movie.setId(int(input(f"set id for \"{movie.title}\":")))
                movies.push(movie)
            else:
                movie = getData(line)
                movies.push(movie)
    
            with open(Locations["left"], "w") as w:
                for line in left:
                    w.write(line + "\n")
        
        with open(Locations["output"], "a") as W:
            for movie in movies:
                W.write(str(movie) + "\n")

    # Creating Output CSV file     
    with open(Locations["output"], "r") as f:
        lines = f.read()
        with open(Locations["csv"], "w") as w:
            w.write("id,title,year,quality,language\n")
            for line in lines.split("\n"):
                if line == "":
                    continue
                #line.replace("", "")
                line = line.split(",")
                settitle = lambda title: f"{title}"
                ide = line[0]
                year = line[2]
                title = settitle(line[1])
                quality = line[3]
                language = line[4]
                w.write(f"{ide},{title},{year},{quality},{language}\n")


def CleanUp():
    os.remove(Locations["left"])
    os.remove(Locations["output"])
    os.remove(Locations["movies"])
    print(f"files ({Locations['left']}, {Locations['output']} {Locations['movies']}) were removed")


def Check(MovieId, Collection):
    try:
        Collection.find({"_id": MovieId})[0]
        return True
    except:
        return False


if __name__ == "__main__":
    # Data parsing
    # - Main()
    # TMP dump clean up
    # - CleanUp()
    # Loading parsed
    movies = LoadMovies(Locations["csv"])
    # Renaming folders
    # - MoveFolders(Locations["base"], movies)
    # Updating database
    MoviesCollection = DB("Movie")
    PostresCollection = DB("Posters")
    LogosCollection = DB("Logos")
    BackdropsCollection = DB("Backdrops")

    count = 0
    start_progress("Inserting into Database")
    for movie in movies:
        count += 1
        progress((100 * count) // len(movies))
        
        if not Check(movie["id"], MoviesCollection):
            #data fetching
            data = FetchMovie(movie["id"])
            RawVideos = FetchVideos(movie["id"])
            # data parsing
            parsedVideos = ParseVideosToArray(RawVideos)
            parsed = ParseMovie(movie, data, parsedVideos)
            # data injection
            Inject(parsed, MoviesCollection)

        parseArtwork = {}
        
        if not Check(movie["id"], PostresCollection) or not Check(movie["id"], LogosCollection) or not Check(movie["id"], BackdropsCollection):
            #data fetching
            RawArtwork = FetchArtwork(movie["id"])

            # data parsing
            parsedArtwork = ParseArtwork(RawArtwork)

        
        if not Check(movie["id"], PostresCollection):
            # data injection
            Inject(parsedArtwork["posters"], PostresCollection)

        if not Check(movie["id"], BackdropsCollection):
            # data injection
            Inject(parsedArtwork["backdrops"], BackdropsCollection)

        if not Check(movie["id"], LogosCollection):
            # data injection
            Inject(parsedArtwork["logos"], LogosCollection)


    end_progress()

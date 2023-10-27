import os
from typing import Any
from Queue import Queue
from Renamer import MoveFolders

os.system("./MoviesGrep.sh")

Locations = {
    "left": "left.txt",
    "output": "./Dump/output.txt",
    "movies": "./Dump/movies.txt",
    "csv": "./Out/movies.csv",
    "base": "./movies"
}


class Movie():
    def __init__(self, title: str, year: int, quality: str):
        self._title = title
        self._year = year
        self._quality = quality
        self._id = 0
    
    def setId(self, id: int):
        self._id = id
    
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, new_title):
        self._title = new_title
    def __str__(self):
        return f"{self._id},'{self._title}',{self._year},'{self._quality}'"


def addToClipBoard(text):
    command = f'echo \"{text.strip()}\" | xclip -selection clipboard'
    os.system(command)

def getData(data: str):
    title = (data.split("(")[0]).strip()
    year = data.split("(")[1].split(")")[0]
    quality = data.split("[")[1].split("]")[0] 
    return Movie(title, year, quality)


def Main():
    left = Queue()
    setId = True

    # Creating output file if it doesn't exist
    if not os.path.exists(Locations["output"]):
        with open(Locations["output"], "w") as f:
            pass

    # Creating left file if it doesn't exist
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
                ide = line.split("#")[1]  
                movie = getData(line)
                movie.setId(ide)
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
            w.write("id,title,year,quality\n")
            for line in lines.split("\n"):
                if line == "":
                    continue
                line.replace("", "")
                line = line.split(",")
                settitle = lambda title: f"{title}"
                ide = line[0]
                year = line[2]
                title = settitle(line[1])
                quality = line[3]
                w.write(f"{ide},{title},{year},{quality}\n")
                #os.remove("left.txt")

if __name__ == "__main__":
    Main()
    MoveFolders(Locations["base"])
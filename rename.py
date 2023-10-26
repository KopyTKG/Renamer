import os
from typing import Any

os.system("./MoviesGrep.sh")


class Queue:
    def __init__(self, start=[]):
        if not start:
            self.__memory = []
        else:
            self.__memory = start

    def set(self, array):
        self.__memory = array

    def push(self, item):
        self.__memory.append(item)
  
    def pop(self) :
        return self.__memory.pop(0)

    def front(self):
        if self.isEmpty():
            return None
        else:
            return(self.__memory[0])
    
    def rear(self):
        if self.isEmpty():
            return None
        else:
            return(self.__memory[-1])
    
    def isEmpty(self):
        return not self.__memory

    def __len__(self):
        return(len(self.__memory))
    
    def __iter__(self):
        for item in self.__memory:
            yield item

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
    if not os.path.exists("output.txt"):
        with open("output.txt", "w") as f:
            pass

    # Creating left file if it doesn't exist
    # File is used to keep memory of untagged movies
    if not os.path.exists("left.txt"):
        with open("movies.txt", "r") as f:
            lines = f.read()
            left.set(lines.split("\n"))
            with open("left.txt", "w") as w:
                for line in left:
                    w.write(line + "\n")
    else:
        with open("left.txt", "r") as f:
            lines = f.read()
            splitted = lines.split("\n")
            if len(splitted) > 1:
                left.set(splitted)
            else:
                setId = False
                print("No movies found")

    if setId:
        for _ in range(len(left)):
            line = left.pop()
            if line == "":
                continue
            if "#" not in line:
                print("No id found")
                movie = getData(line)
                addToClipBoard(movie.title)
                try:
                    movie.setId(int(input(f"set id for \"{movie.title}\":")))
                except:
                    pass
            else:
                ide = line.split("#")[1]  
                movie = getData(line)
                movie.setId(ide)
    
            with open("output.txt", "a") as W:
                W.write(str(movie) + "\n")
                with open("left.txt", "w") as w:
                    for line in left:
                        w.write(line + "\n")

    # Creating Output CSV file     
    with open("output.txt", "r") as f:
        lines = f.read()
        with open("movies.csv", "w") as w:
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
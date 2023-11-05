import os
import csv



def LoadMovies(file):
    movies = []
    with open('./Out/movies.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            movies.append(row)
    movies.pop(0)


def MoveFolders(folder, movies):
    for movie in movies:
        quality = movie[3].replace("'", "")
        year = movie[2]
        title = movie[1][1:-1]
        ide = movie[0].replace("'", "")

        NewName = f"{folder}/{title} ({year}) [{quality}] #{ide}"
        OldName = f"{folder}/{title} ({year}) [{quality}]"

        if not os.path.exists(NewName):
            os.rename(OldName, NewName)


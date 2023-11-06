import os
import csv



def LoadMovies(file):
    movies = []
    with open('./Out/movies.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            quality = row[3].replace("'", "")
            year = row[2]
            title = row[1][1:-1]
            ide = row[0].replace("'", "")
            if ide == "id":
                continue
            movies.append({
                "id": int(ide),
                "title": title,
                "year": int(year),
                "quality": quality
            })
    return movies


def MoveFolders(folder, movies):
    for movie in movies:
        NewName = f"{folder}/{movie['title']} ({movie['year']}) [{movie['quality']}] #{movie['id']}"
        OldName = f"{folder}/{movie['title']} ({movie['year']}) [{movie['quality']}]"

        if not os.path.exists(NewName):
            print(f"moving {OldName} to {NewName}")
            os.rename(OldName, NewName)


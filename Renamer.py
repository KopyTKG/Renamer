import os
import csv
from progress import start_progress, end_progress, progress


def LoadMovies(Path):
    movies = []
    with open(Path, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            language = row[4].replace("'", "")
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
                "quality": quality,
                "language": language
            })
    
    return movies


def MoveFolders(folder, movies):
    start_progress("Renaming Folders")
    count = 0
    for movie in movies:
        count += 1        
        NewName = f"{folder}/{movie['title']} ({movie['year']}) [{movie['quality']}] #{movie['id']} <{movie['language']}>"
        OldName = f"{folder}/{movie['title']} ({movie['year']}) [{movie['quality']}]"

        if not os.path.exists(NewName):
            os.rename(OldName, NewName)
        
        progress((100 * count) // len(movies))
    end_progress()



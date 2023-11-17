# Renamer [![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

Backend application for [MovieDB](https://github.com/KopyTKG/MovieDB)


## Folder layout
`../Movies/` folder used to store all Movie forlders

`Dump/` folder for data to be processed

`Out/` folder storing all output CSV files.(`Genres.csv` and `movies.csv`)

`classes/` internal folder with all python files needed for the app it self.

## Movie Naming
for app to function properly you need to name all of your movies (stored in folder)

`name (year) [quality]`

after the app is finished all movies will be named.

`name (year) [quality] #id <language>`



## Deployment

To deploy this project make sure that:

1. `.env` file is created and filled with
```env
Auth="TMDB API token"
CONNECTION_STRING="mongodb://user:password@ip:port"
```

2. create `venv` by running
```bash
# Linux
python -m venv venv
source venv/bin/activate
```
```bash
# Windows
python -m venv venv
venv/scripts/activate
```

3. Install all packages
```bash
pip install -r reqs.txt
```

4. On linux add permitions to the `MoviesGrep.sh`
```bash
sudo chmod u+x MoviesGrep.sh
```

5. Run the app with
```bash
python Main.py
```
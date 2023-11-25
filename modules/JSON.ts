import fs from 'fs'

class JSONFile {
  private _movies: Array<unknown>

  constructor() {
    this._movies = []
  }

  public push(data: unknown) {
    if (!data) {
      return
    }
    //id,title,year,quality,language
    const movie = data.toString().split(',')
    const parsed = {
      id: movie[0],
      title: movie[1],
      year: movie[2],
      quality: movie[3],
      language: movie[4],
    }
    this._movies.push(parsed)
  }

  public WriteFile(path: string) {
    const json = {
      movies: this._movies,
    }
    fs.appendFileSync(path, JSON.stringify(json))
  }

  public ReadFile(path: string) {
    const raw = fs.readFileSync(path)
    const movies = raw.toString()
    const jsonMovies = JSON.parse(movies)

    const parsed = []
    jsonMovies.movies.forEach((movie) => {
      parsed.push(
        movie.id +
          ',' +
          movie.title +
          ',' +
          movie.year +
          ',' +
          movie.quality +
          ',' +
          movie.language,
      )
    })

    return parsed
  }
}

export default JSONFile

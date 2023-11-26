import fs from 'fs'

class JSONFile {
  private _movies: Array<unknown>

  constructor() {
    this._movies = []
  }

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  public push(data: any) {
    if (!data) {
      return
    }
    //id,title,year,quality,language
    const parsed = {
      id: data.id,
      title: data.title,
      year: data.year,
      quality: data.quality,
      language: data.language,
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

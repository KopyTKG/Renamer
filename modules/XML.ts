import fs from 'fs'

class XMLFile {
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
    const parsed = `<movie>\n <id>${movie[0]}</id>\n <title>${movie[1]}</title>\n <year>${movie[2]}</year>\n <quality>${movie[3]}</quality>\n <language>${movie[4]}</language>\n </movie>`
    this._movies.push(parsed)
  }

  public WriteFile(path: string) {
    fs.appendFileSync(path, `<movies>\n`)

    this._movies.forEach((movie) => {
      fs.appendFileSync(path, `${movie}\n`)
    })
    fs.appendFileSync(path, `</movies>\n`)
  }

  public ReadFile(path: string) {
    const raw = fs.readFileSync(path)
    let movies = raw.toString()
    movies = movies.replaceAll('<movies>', '').replaceAll('</movies>', '')

    movies = movies.replaceAll('movie', '')
    movies = movies.replaceAll('<>', '')
    movies = movies.replaceAll('<id>', '-').replaceAll('</id>', ',')
    movies = movies.replaceAll('<title>', '').replaceAll('</title>', ',')
    movies = movies.replaceAll('<year>', '').replaceAll('</year>', ',')
    movies = movies.replaceAll('<quality>', '').replaceAll('</quality>', ',')
    movies = movies.replaceAll('<language>', '').replaceAll('</language>', ';')

    movies = movies.replaceAll('\n', '')
    movies = movies.replaceAll(', ', ',').replaceAll('; ', '').replaceAll(' -', '')

    const moviesParsed = movies.split('</>')
    moviesParsed.pop()
    return moviesParsed
  }
}

export default XMLFile

import fs from 'fs'

class XMLFile {
  private _movies: Array<unknown>

  constructor() {
    this._movies = []
  }

  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  public push(data: any) {
    if (!data) {
      return
    }
    const id = `<id>${data.id}</id>`
    const title = `<title>${data.title}</title>`
    const year = `<year>${data.year}</year>`
    const quality = `<quality>${data.quality}</quality>`
    const language = `<language>${data.language}</language>`

    const parsed = `<movie>\n ${id}\n ${title}\n ${year}\n ${quality}\n ${language}\n</movie>`
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

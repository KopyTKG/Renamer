import fs from 'fs'
import LogCreate from './LogCreate'

class FolderCreater {
  private _data = {
    movies: [],
  }
  constructor(private logger: LogCreate) {
    this.logger.on('logCreated', () => {
      this.Load()
      this.Create()
    })
  }

  public Load() {
    this._data = JSON.parse(fs.readFileSync('./Out/zdump.json', 'utf8'))
  }

  public IsPossible(path: string): boolean {
    return fs.existsSync('./Data/' + path)
  }
  public Create(): void {
    this._data.movies?.forEach((path) => {
      if (!this.IsPossible(JSON.stringify(path))) {
        fs.mkdirSync('./Data/' + JSON.stringify(path))
      }
    })
  }
}

export default FolderCreater

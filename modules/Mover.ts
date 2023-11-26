import fs from 'fs'
import LogCreate from './LogCreate'
import Settings from './Settings'

class FolderCreater {
  private _data = {
    movies: [],
  }
  private settings = Settings.Instance.Data

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
    return fs.existsSync(this.settings.TestingFolder + path)
  }
  public Create(): void {
    this._data.movies?.forEach((path) => {
      if (!this.IsPossible(JSON.stringify(path))) {
        fs.mkdirSync(this.settings.TestingFolder + JSON.stringify(path))
      }
    })
  }
}

export default FolderCreater

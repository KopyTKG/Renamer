import Mover from './modules/Mover'
import Reader from './modules/Reader'
import MovieCollection from './modules/MovieStucture'
import LogCreate from './modules/LogCreate'
import Settings from './modules/Settings'

class Facade {
  private _Reader: Reader
  private _mover: Mover

  constructor() {
    this._Reader = new Reader()
    this._mover = new Mover(LogCreate.Instance())
    Settings.Instance
  }

  public Main() {
    const list = this._Reader.ReadFolder('../Movies/')
    const movies = new MovieCollection()
    list.forEach((line) => {
      movies.push(line)
    })
    const log = LogCreate.Instance()
    log.Data = movies
    log.CreateLogs()
  }
}

new Facade().Main()

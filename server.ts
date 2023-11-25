import Mover from './modules/Mover'
import Reader from './modules/Reader'
import ListedFolder from './modules/Adapter'
import LogCreate from './modules/LogCreate'

class Facade {
  private _Reader: Reader
  private _mover: Mover

  constructor() {
    this._Reader = new Reader()
    this._mover = new Mover(LogCreate.Instance())
  }

  public Main() {
    const list = this._Reader.ReadFolder('../Movies/')
    const listedFolder = new ListedFolder(list)
    const log = LogCreate.Instance()
    log.Data = listedFolder.StringToCSV()
    log.CreateLogs()
  }
}

new Facade().Main()

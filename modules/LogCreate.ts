import EventEmitter from 'events'
import OutputHandler from './File.director'
import XMLBuilder from './XML.builder'
import JSONBuilder from './JSON.builder'
import Settings from './Settings'
import MovieCollection from './MovieStucture'

class LogCreate extends EventEmitter {
  private static _instance: LogCreate

  private _data: MovieCollection

  private _json: JSONBuilder
  private _xml: XMLBuilder
  private _director: OutputHandler

  private constructor() {
    super()
    this._data = new MovieCollection()
    this._json = new JSONBuilder()
    this._xml = new XMLBuilder()
    this._director = new OutputHandler()
  }

  public static Instance(): LogCreate {
    if (!this._instance) {
      this._instance = new LogCreate()
    }
    return this._instance
  }

  public set Data(data: MovieCollection) {
    this._data = data
  }

  public CreateLogs(): void {
    if (!this._data) {
      return
    }
    const config = Settings.Instance.Data
    const path = `${config.LogFolder}zdump`
    this._director.Filename = path

    this._director.FileType = this._json
    this._director.WriteOutput(this._data)

    this._director.FileType = this._xml
    this._director.WriteOutput(this._data)

    this.emit('logCreated', 'Log Create')
  }
}

export default LogCreate

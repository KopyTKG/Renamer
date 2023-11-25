import { log } from 'console'
import EventEmitter from 'events'
import OutputHandler from './File.director'
import XMLBuilder from './XML.builder'
import JSONBuilder from './JSON.builder'

class LogCreate extends EventEmitter {
  private static _instance: LogCreate

  private _data: Array<string>

  private _json: JSONBuilder
  private _xml: XMLBuilder
  private _director: OutputHandler

  private constructor() {
    super()
    this._data = []
    this._json = new JSONBuilder()
    this._xml = new XMLBuilder()
    this._director = new OutputHandler()

    this.on('newListener', (event: string) => {
      log(event)
    })
  }

  public static Instance(): LogCreate {
    if (!this._instance) {
      this._instance = new LogCreate()
    }
    return this._instance
  }

  public set Data(data: Array<string>) {
    this._data = data
  }

  public CreateLogs(): void {
    if (!this._data) {
      return
    }
    const path = './Out/zdump'
    this._director.Filename = path

    this._director.FileType = this._json
    this._director.WriteOutput(this._data)

    this._director.FileType = this._xml
    this._director.WriteOutput(this._data)

    this.emit('logCreated', 'Log Create')
  }
}

export default LogCreate

import OutputHandler from './modules/File.director'
import JSONBuilder from './modules/JSON.builder'
import Mover from './modules/Mover'
import Reader from './modules/Reader'
import XMLBuilder from './modules/XML.builder'
import ListedFolder from './modules/Adapter'

class Facade {
  private _Reader: Reader
  private _json: JSONBuilder
  private _xml: XMLBuilder
  private _mover: Mover
  private _director: OutputHandler

  constructor() {
    this._Reader = new Reader()
    this._json = new JSONBuilder()
    this._xml = new XMLBuilder()
    this._mover = Mover.Instance
    this._director = new OutputHandler()
  }

  public Main() {
    const list = this._Reader.ReadFolder('../Movies/')
    const listedFolder = new ListedFolder(list)

    const path = './Out/zdump'
    this._director.Filename = path

    this._director.FileType = this._json
    this._director.WriteOutput(listedFolder.StringToCSV())

    this._director.FileType = this._xml
    this._director.WriteOutput(listedFolder.StringToCSV())
  }
}

new Facade().Main()

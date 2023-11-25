import IFile from '../interfaces/IFIle'

class OutputHandler {
  private _builder: IFile
  private _filename: string

  constructor() {
    this._builder = null
    this._filename = ''
  }

  public set FileType(builder: IFile) {
    this._builder = builder
  }

  public set Filename(filename: string) {
    this._filename = filename
  }

  public WriteOutput(data: Array<unknown>): void {
    if (!this._builder) {
      return
    }
    if (this._filename) {
      this._builder.Create(this._filename)
      data.map((movie) => {
        this._builder.Add(movie)
      })
      this._builder.Flush(this._filename)
    } else {
      return
    }
  }

  public ReadOutput(): Array<unknown> {
    if (!this._builder) {
      return
    }
    if (this._filename) {
      return this._builder.Read(this._filename)
    } else {
      return []
    }
  }
}

export default OutputHandler

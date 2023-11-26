import IFile from '../interfaces/IFIle'
import MovieCollection from './MovieStucture'

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

  public WriteOutput(data: MovieCollection): void {
    if (!this._builder) {
      return
    }
    if (this._filename) {
      this._builder.Create(this._filename)
      const iter = data.getIterator()
      while (iter.valid()) {
        this._builder.Add(iter.current())
        iter.next()
      }
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

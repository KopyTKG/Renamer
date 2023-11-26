import IFile from '../interfaces/IFIle'
import fs from 'fs'
import JSONFile from './JSON'

class JSONBuilder implements IFile {
  private _json: JSONFile
  private _extension = '.json'

  constructor() {
    this.reset()
  }

  public reset(): void {
    this._json = new JSONFile()
  }

  public Create(path: string): void {
    fs.writeFileSync(path + this._extension, '')
  }

  public Add(data: unknown): void {
    this._json.push(data)
  }

  public Flush(path: string): void {
    this._json.WriteFile(path + this._extension)
  }

  public Read(path: string): Array<unknown> {
    return this._json.ReadFile(path + this._extension)
  }
}

export default JSONBuilder

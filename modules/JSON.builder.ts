import IFile from '../interfaces/IFIle'
import fs from 'fs'
import JSONFile from './JSON'

class JSONBuilder implements IFile {
  private _xml: JSONFile
  private _extension = '.json'

  constructor() {
    this.reset()
  }

  public reset(): void {
    this._xml = new JSONFile()
  }

  public Create(path: string): void {
    fs.writeFileSync(path + this._extension, '')
  }

  public Add(data: unknown): void {
    this._xml.push(data)
  }

  public Flush(path: string): void {
    this._xml.WriteFile(path + this._extension)
  }

  public Read(path: string): Array<unknown> {
    return this._xml.ReadFile(path + this._extension)
  }
}

export default JSONBuilder

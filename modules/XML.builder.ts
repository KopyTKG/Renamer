import IFile from '../interfaces/IFIle'
import XMLFile from './XML'
import fs from 'fs'

class XMLBuilder implements IFile {
  private _xml: XMLFile
  private _extension = '.xml'

  constructor() {
    this.reset()
  }

  public reset(): void {
    this._xml = new XMLFile()
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

export default XMLBuilder

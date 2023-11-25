import ITypeConverter from '../interfaces/ITypeConverter'

class Converter implements ITypeConverter {
  public StringToCSV(data: Array<string>): Array<string> {
    const newData = []
    data.map((movie) => {
      const id = movie.split('#')[1].split(' ')[0]
      const title = movie.split(' (')[0]
      const year = movie.split(' (')[1].split(')')[0]
      const quality = movie.split(' [')[1].split(']')[0]
      const language = movie.split(' <')[1].split('>')[0]

      newData.push(id + ',' + title + ',' + year + ',' + quality + ',' + language)
    })
    return newData
  }
}

class ListedFolder {
  private _list: Array<string>
  private _converter: Converter
  constructor(list: Array<string>) {
    this._list = list
    this._converter = new Converter()
  }

  public StringToCSV(): Array<string> {
    return this._converter.StringToCSV(this._list)
  }
}

export default ListedFolder

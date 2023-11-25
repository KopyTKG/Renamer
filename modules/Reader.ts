import fs from 'fs'

class Reader {
  constructor() {}
  public ReadFolder(path: string): Array<string> {
    const files = fs.readdirSync(path)
    return files
  }
}

export default Reader

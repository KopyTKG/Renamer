import fs from 'fs'

class Settings {
  private static _instance: Settings
  private _data = {
    DataFolder: '',
    TestingFolder: '',
    LogFolder: '',
  }
  private constructor() {
    this.Load()
  }

  public static get Instance(): Settings {
    if (!this._instance) {
      this._instance = new Settings()
    }
    return this._instance
  }

  public get Data() {
    return this._data
  }

  private Load() {
    const data = fs.readFileSync('./settings.cfg', 'utf8')
    const splitted = data.split('\n')
    splitted.pop()
    splitted.forEach((line) => {
      const items = line.split('=')
      this._data[items[0].replace(' ', '')] = items[1].replace(' ', '')
    })
  }
}

export default Settings

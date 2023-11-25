import fs from 'fs'

class Mover {
  private oldName: string
  private newName: string

  private static instance: Mover

  private constructor() {}

  public static get Instance(): Mover {
    if (!this.instance) {
      this.instance = new Mover()
    }
    return this.instance
  }

  public set OldName(oldName: string) {
    this.oldName = oldName
  }

  public set NewName(newName: string) {
    this.newName = newName
  }

  public get IsMovePossible(): boolean {
    return fs.existsSync(this.oldName)
  }
  public Move() {
    if (!this.oldName || !this.newName) {
      throw new Error('Old name or new name not set')
    }
    fs.renameSync(this.oldName, this.newName)
  }
}

export default Mover

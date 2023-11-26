import { Aggregator, Iterator } from '../interfaces/Iterator'

class MovieStucture implements Iterator<unknown> {
  private _collection: MovieCollection
  private _position: number = 0
  private _reverse: boolean = false

  constructor(collection: MovieCollection, reverse: boolean = false) {
    this._collection = collection

    if (reverse) {
      this._position = collection.count() - 1
      this._reverse = true
    }
  }

  rewind(): void {
    this._position = this._reverse ? this._collection.count() - 1 : 0
  }

  next(): void {
    if (this._reverse) {
      this._position = this._position - 1
    }
    this._position = this._position + 1
  }

  prev(): void {
    this._position = !this._reverse ? --this._position : ++this._position
  }

  current(): unknown {
    return this._collection.items[this._position]
  }

  valid(): boolean {
    if (this._reverse) {
      return this._position >= 0
    }

    return this._position < this._collection.count()
  }

  first(): unknown {
    return this._reverse
      ? this._collection.items[this._collection.count() - 1]
      : this._collection.items[0]
  }

  last(): unknown {
    return !this._reverse
      ? this._collection.items[this._collection.count() - 1]
      : this._collection.items[0]
  }

  key(): number {
    return this._position
  }
}

class MovieCollection implements Aggregator<unknown> {
  private _collection: Array<unknown> = []
  private currentId: number = 0

  getIterator(): Iterator<unknown> {
    return new MovieStucture(this)
  }

  getReverseIterator(): Iterator<unknown> {
    return new MovieStucture(this, true)
  }

  count(): number {
    return this._collection.length
  }

  push(data: string): void {
    if (data.includes('#')) {
      const id = data.toString().split('#')[1].split(' ')[0]
      const title = data.toString().split(' (')[0]
      const year = data.toString().split(' (')[1].split(')')[0]
      const quality = data.toString().split('[')[1].split(']')[0]
      const language = data.toString().split('<')[1].split('>')[0]
      const parsed = {
        id: id,
        title: title,
        year: year,
        quality: quality,
        language: language ? language : 'en-US',
      }
      this._collection.push(parsed)
    } else {
      const title = data.toString().split(' (')[0]
      const year = data.toString().split(' (')[1].split(')')[0]
      const quality = data.toString().split('[')[1].split(']')[0]

      const parsed = {
        id: this.currentId,
        title: title,
        year: year,
        quality: quality,
        language: 'en-US',
      }
      this._collection.push(parsed)
    }
  }

  pop(): unknown {
    return this._collection.pop()
  }

  public get items(): unknown {
    return this._collection
  }
}

export default MovieCollection

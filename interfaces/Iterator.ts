interface Iterator<T> {
  next(): void
  prev(): void
  current(): T
  rewind(): void

  key(): number

  valid(): boolean

  first(): T
  last(): T
}

interface Aggregator<T> {
  getIterator(): Iterator<T>
}

export { Iterator, Aggregator }

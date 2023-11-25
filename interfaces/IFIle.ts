interface IFile {
  reset(): void
  Create(path: string): void
  Add(data: unknown): void
  Flush(path: string): void
  Read(path: string): Array<unknown>
}

export default IFile

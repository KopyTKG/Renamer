## Design patterns used

1. Singleton -> [LogCreate](./modules/LogCreate.ts)
2. Fasade -> [Server](./server.ts)
2. Builder -> [XMLBuilder](./modules/XML.builder.ts) | [JSONBuilder](./modules/JSON.builder.ts) 
3. Iterator -> [MovieCollection](./modules/MovieStucture.ts)
4. Observer -> Emitor: [LogCreate](./modules/LogCreate.ts) | Subscriber: [FolderCreater](./modules/Mover.ts)
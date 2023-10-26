
class Queue:
    def __init__(self, start=[]):
        if not start:
            self.__memory = []
        else:
            self.__memory = start

    def set(self, array):
        self.__memory = array

    def push(self, item):
        self.__memory.append(item)
  
    def pop(self) :
        return self.__memory.pop(0)

    def front(self):
        if self.isEmpty():
            return None
        else:
            return(self.__memory[0])
    
    def rear(self):
        if self.isEmpty():
            return None
        else:
            return(self.__memory[-1])
    
    def isEmpty(self):
        return not self.__memory

    def __len__(self):
        return(len(self.__memory))
    
    def __iter__(self):
        for item in self.__memory:
            yield item

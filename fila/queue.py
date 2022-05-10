from node import Node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
        
    def push(self, elem):
        #metodo para inserir elementos na fila 
        node = Node(elem)
        if self.tail is None:
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        if self.head is None:
            self.head = node
        self._size = self._size + 1
    
    def pop(self):
        # metodo para remover o elemento da fila
        if self.head is not None:
            elem = self.head.data
            self.head = self.head.next
            self._size = self._size - 1
            return elem
        raise IndexError("The queue is empty")
    
    def peek(self):
        # retorna o começo da fila
        if self.head is not None:
            elem = self.head.data
            return elem
        raise IndexError("The queue is empty")
        
    def __len__(self):
        # retorna o tamanho da fila 
        return self._size
    
    def __repr__(self):
        # apresenta os elementos da fila
        if self.head is not None:
            r = ""
            pointer = self.head
            while(pointer):
                r = r + str(pointer.data) + ", "
                pointer = pointer.next
            return r
        raise IndexError("The queue is empty")

    def __str__(self):
        return self.__repr__()  
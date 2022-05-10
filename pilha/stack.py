from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
        
    def push(self, elem):
        #metodo para inserir elementos na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self.size + 1
    
    def pop(self):
        # metodo para remover o elemento no topo da pilha 
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self.size - 1
            return node.data
        raise IndexError("The stack is empty")
    
    def peek(self):
        # metodo para observar o topo da pilha
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")
        
    def __len__(self):
        # retorna o tamanho da lista
        return self._size
    
    def __repr__(self):
        # metodo para mostrar os elementos da lista
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r 

    def __str__(self):
        return self.__repr__()  
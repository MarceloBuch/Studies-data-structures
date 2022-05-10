#criação de listas encadeadas

from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elem):
        if self.head:
            # inserção quando a lista já possui elementos
            pointer = self.head # variavel de apoio para ir passando os locais da lista
            while(pointer.next):# verifica se existe o proximo elemento
                pointer = pointer.next # se o elemento existe, o pointer passa a para o próximo elemento e o while se repete
            pointer.next = Node(elem) # quando o pointer chega ao fim da lista ele cria o proximo item da lista
            self._size = self._size + 1
        else:
            # primeira inserção 
            self.head = Node(elem)
        self._size = self._size + 1
        
    def _getNode(self, index):
        pointer = self.head # é atribuido o head a variavel pointer
        for i in range(index):# o for procura o index que foi pedido
            if pointer:# verifica se a lista não esta com a primeira posição vazia
                pointer = pointer.next # a variavel pointer passa para o prox elemento até chegar onde deve
            else:
                raise IndexError("list index out of range") # se estiver com a lista vazia é retornado esse erro
        return pointer
        
    def __len__(self):
        # retorna o tamanho da lista
        return self._size
    
    def __getitem__(self, index):
        # função para retornar um elemento
        # para utilizar - a = lista[4] - só passar o index
        pointer = self._getNode(index)
        if pointer:
            return pointer.data # mostra o valor da posição
        else:
            raise IndexError("list index out of range") # se estiver com a lista vazia é retornado esse erro
            
    
    def __setitem__(self, index, elem):
        # função para modificar um elemento
        # para utilizar - a = lista[4, 3] - passar o index do elemento que ser trocado e o proprio valor que ser trocado
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elem #depois de achar, ele muda o valor do encontrado pelo valor que foi passado no elem
        else:
            raise IndexError("list index out of range") # se estiver com a lista vazia é retornado esse erro
        
    def index(self, elem):
        # metodo de busca linear 
        pointer = self.head
        i = 0 
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i = i + 1
            raise ValueError("{} is not in list".format(elem))
    
    def insert(self, index, elem):
        # metodo para inserir elementos em qualquer parte da lista
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node = Node(elem)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1
        
    def remove(self, elem):
        # metodo para remover o elemento escolhido
        if self.head == None:
            raise ValueError("{} is not in list".format(elem))
        elif self.head.data == elem:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError("{} is not in list".format(elem))   
    
def __repr__(self):
    # metodo para mostrar os elementos da lista
    r = ""
    pointer = self.head
    while(pointer):
        r = r + str(pointer.data) + "-->"
        pointer = pointer.next
    return r 

def __str__(self):
    return self.__repr__()  
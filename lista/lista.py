# busca linear em lista em alocação linear

lista = [1,2,3,45,2938,34]
elem = 5

def busca(lista, elem):
    '''essa função retorna o indice do elemento se ele estiver na lista, caso contrário, ele retorna none'''
    for i in range(len(lista)):
        if lista[i] == elem:
            return i
    return None

resultado = busca(lista, elem)
if resultado is not None:
    print("o inidice do elemento é ",resultado)
else:
    print("o elemento não foi encontrado na lista")
    
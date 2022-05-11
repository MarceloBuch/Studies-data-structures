import random
from tree import BinarySearchTree

random.seed(77)

values = random.sample(range(1,1000), 42)

bst = BinarySearchTree()
for c in values:
    bst.insert(c)

#bst.inorder_traversal()

items = [1, 30, 188, 150, 570]
for item in items:
    r = bst.search(item)
    if r is None:
        print(item, "Não encontrado")
    else:
        print(r.root.data, "encontrado")
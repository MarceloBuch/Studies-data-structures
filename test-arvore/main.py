from tree import BinarySearchTree

bst = BinarySearchTree()
for i in range(0, 101):
    bst.insert(i)

bst.postorder_traversal()

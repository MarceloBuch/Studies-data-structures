class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data = None, node = None):
        if node:
            self.root = node
        elif data:
            self.root = data
        else:
            self.root = None

    def inorder_traversal(self, node=None):
        if node is None:
            node=self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end =' ')
        if node.right:
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
    
class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value % 2 == 1:
                x = x.left
            elif value % 2 == 0:
                x = x.right
        if parent is None: 
            self.root = Node(value)
        elif value % 2 == 1:
            parent.left = Node(value)
        elif value % 2 == 0:
            parent.right = Node(value)

    def search(self, value, node=0):
        if node == 0:
            node = self.root
        if node is None:
            return node
        if node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value, node.right)

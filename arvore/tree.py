class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self, data=None, node = None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    #percurso em ordem simétrica        
    def simetric_traversal(self, node=None):
        if node is None:
            node=self.root
        if node.left:
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)

    #percurso em pós-ordem
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    #altura da árvore
    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0 
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    def inorder_traversal(self, node=None):
        if node is None:
            node=self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node, end =' ')
        if node.right:
            self.inorder_traversal(node.right)
    
class BinarySearchTree(BinaryTree):
    def insert(self, value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data:
                x = x.left
            else:
                x = x.right
        if parent is None:
            self.root = Node(value)
        elif value < parent.data:
            parent.left = Node(value)
        else:
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
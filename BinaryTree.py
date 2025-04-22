class BinaryTree:
    ''' Binary Tree Implementation'''
    def __init__(self, root=None):
        self.root = None

# ----- Recurisve Traversal Methods-------
    def inorder_traversal(self, node=None):
        '''Performs in-order traversal: left subtree -> root -> right subtree'''
        if node is None:
            return
        
        if node:
            if node.left:
                self.inorder_traversal(node.left)
            print(node.key, end=' ')
        
    def preorder_traversal(self, node=None):
        '''Performs pre-order traversal: root -> left subtree -> right subtree'''
        if node is None:
            return
        
        if node:
            print(node.key, end=' ')
            if node.left:
                self.preorder_traversal(node.left)
            if node.right:
                self.preorder_traversal(node.right)
        
    def postorder_traversal(self, node=None):
        '''Performs pre-order traversal: left subtree -> right subtree -> root'''
        if node is None:
            return
        
        if node:
            if node.left:
                self.postorder_traversal(node.left)
            if node.right:
                self.postorder_traversal(node.right)
            print(node.key, end=' ')
            

"""
    def insert(self, key):
        ''' Insert a node into the Binary Tree'''
        if self.root is None:
            self.root = Node(data)
            return
        if 

    def collect_data(self):
        def traverse(node):
            if node is None:
                return []
            return traverse(node.left) + [node.data] + traverse(node.right)
        return traverse(self.root)

'''

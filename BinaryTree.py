class BinaryTree:
    ''' Binary Tree Implementation'''
    def __init__(self, root=None):
        self.root = None

# ----- Recurisve Traversal Methods-------
    def inorder_traversal(self, node=None):
        if node is None:
          return
        



'''
class RegularBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data, path=""):
        """ Insert data based on path (e.g., 'LLR' -> left->left->right) """
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        for direction in path[:-1]:
            if direction == 'L':
                if current.left is None:
                    current.left = Node(None)
                current = current.left
            elif direction == 'R':
                if current.right is None:
                    current.right = Node(None)
                current = current.right

        if path[-1] == 'L':
            current.left = Node(data)
        else:
            current.right = Node(data)

    def collect_data(self):
        def traverse(node):
            if node is None:
                return []
            return traverse(node.left) + [node.data] + traverse(node.right)
        return traverse(self.root)

'''

class BinaryTree:
    def __init__(self, root):
        self.root = root

# ----- Recurisve Traversal Methods-------
    def inorder_traversal(self, node):
        if node: # <-- This is the crucial base case check
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node: # <-- This is the crucial base case check
            print(node.key, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node: # <-- This is the crucial base case check
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.key, end=' ')
   
    # ----- Print Tree wiht Indentation------
    def print_tree(self, node, level=0, prefix="Root:"):
        if node:  # <-- This is the crucial base case check
            print(" " * (5 * level) + prefix + str(node.key))
            if node.left or node.right:
                self.print_tree(node.left, level + 1, "L----")
                self.print_tree(node.right, level + 1, "R----")
                
#-------------------------------------------------------------
# Create a test tree manually                                #
#         A                                                  #
#        / \                                                 #
#       B   C                                                #
#      / \   \                                               #
#     D  E    F                                              #
#                                                            #
# Print the nodes in-order, pre-order, post-order            #
#                                                            #
# Print the manually created binary tree with indentation    #
#------------------------------------------------------------#

if __name__ == "__main__":

    bt = BinaryTree() # Instantiate an object of BinaryTree
    bt.root = Node('A')
    bt.root.left = Node('B')
    bt.root.right = Node('C')
    bt.root.left.left = Node('D')
    bt.root.left.right = Node('E')
    bt.root.right.right = Node('F')

    
    print("In-order Traversal:")
    bt.inorder_traversal(bt.root)
    print()

    print("Pre-order Traversal:")
    bt.preorder_traversal(bt.root)
    print()

    print("Post-order Traversal:")
    bt.postorder_traversal(bt.root)
    print()


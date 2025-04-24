from Node import Node

class BinaryTree:
    def __init__(self, root):
        self.root = root

# ----- Recurisve Traversal Methods-------
    def inorder(self, node):
        if node: # <-- This is the crucial base case check
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node: # <-- This is the crucial base case check
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node: # <-- This is the crucial base case check
            self.postorder(node.left)
            self.postorder(node.right)
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

    bt = BinaryTree(Node('A')) # Instantiate an object of BinaryTree
    bt.root.left = Node('B')
    bt.root.right = Node('C')
    bt.root.left.left = Node('D')
    bt.root.left.right = Node('E')
    bt.root.right.right = Node('F')

    
    print("In-order Traversal:")
    bt.inorder(bt.root)
    print()

    print("Pre-order Traversal:")
    bt.preorder(bt.root)
    print()

    print("Post-order Traversal:")
    bt.postorder(bt.root)
    print()

    print()
    print("Print Tree:")
    bt.print_tree(bt.root)

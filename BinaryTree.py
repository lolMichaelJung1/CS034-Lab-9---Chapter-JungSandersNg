class BinaryTree:
    def __init__(self, root):
        self.root = root
        
# ----- Recurisve Traversal Methods-------
    def inorder_traversal(self, node):
        if node: # <-- This is the crucial base case check
            self.inorder_traversal(node.left)
            print(node.data, end=' ')
            self.inorder_traversal(node.right)

    def preorder_traversal(self, node):
        if node: # <-- This is the crucial base case check
            print(node.data, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node: # <-- This is the crucial base case check
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=' ')

    # ----- Print Tree wiht Indentation------
    def print_tree(self, node=None, indent="", position="root"):
        # Implementation for print_tree
        if node: # <-- This is the crucial base case check
            print(f"{indent}[{position}] - {node.key}")
            if node.left or node.right:
                self.print_tree(node.left, indent + "       ", "L")
                self.print_tree(node.right, indent + "       ", "R")


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


    bt = MyBinaryTree() # Instantiate the subclass
    bt.root = bt.Node('A')
    bt.root.left = bt.Node('B')
    bt.root.right = bt.Node('C')
    bt.root.left.left = bt.Node('D')
    bt.root.left.right = bt.Node('E')
    bt.root.right.right = bt.Node('F')

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


'''

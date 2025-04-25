# Group Members: Michael Jung (ID:10680322), Timothy Sanders (??), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------


from TreeNode import Node

# --- BinaryTree Class ---
# A base class for general binary tree operations. BST inherits from this.
class BinaryTree:
    # Constructor for the BinaryTree class
    def __init__(self, root=None):
        """
        Initializes a binary tree.

        Args:
            root: The root node of the tree. Defaults to None (empty tree).
        """
        self.root = root # The root node of the tree

    # In-order traversal method (Recursive)
    # Visits left subtree, then the current node, then the right subtree.
    # Typically results in sorted order for a BST.
    def inorder(self, node=None):
        """
        Performs an in-order traversal starting from the given node (or root).
        Prints node values during traversal.

        Args:
            node: The current node to start the traversal from. Defaults to
                  the tree's root if not specified.
        """
        # Recursive step (only if the current node is valid)
        if node: # <-- This is the crucial base case check (if node is not None)
            self.preorder(node.left) # Recurse on left child
            print(node.value, end=' ')  # Visit the current node (print its value)
            self.preorder(node.right) # Recurse on right child

    # Pre-order traversal method (Recursive)
    # Visits the current node, then the left subtree, then the right subtree.
    # Useful for copying/recreating the tree structure.
    def preorder(self, node=None):
        """
        Performs a pre-order traversal starting from the given node (or root).
        Prints node values during traversal.

        Args:
            node: The current node to start the traversal from. Defaults to
                  the tree's root if not specified.
        """
        # Recursive step (only if the current node is valid)
        if node: # <-- This is the crucial base case check (if node is not None)
            print(node.value, end=' ')  # Visit the current node (print its value)
            self.preorder(node.left) # Recurse on left child
            self.preorder(node.right) # Recurse on right child


    # Post-order traversal method (Recursive)
    # Visits the left subtree, then the right subtree, then the current node.
    # Useful for deleting the tree (delete children before parent).
    def postorder(self, node=None):
        """
        Performs a post-order traversal starting from the given node (or root).
        Prints node values during traversal.

        Args:
            node: The current node to start the traversal from. Defaults to
                  the tree's root if not specified.
        """
        # Recursive step (only if the current node is valid)
        if node: # <-- This is the crucial base case check (if node is not None)
            self.preorder(node.left) # Recurse on left child
            self.preorder(node.right) # Recurse on right child
            print(node.value, end=' ')  # Visit the current node (print its value)


    # Method to print the tree structure visually
    def print_tree(self, node=None, level=0, prefix='Root:'):
        """
        Prints a visual representation of the tree structure.
        Args:
            node: The current node being printed. Defaults to the tree's root.
            level: The depth of the current node, used for indentation.
            prefix: A string prefix indicating the node's relationship to its parent
                    ('Root:', 'L----', 'R----').
        """
        if node: # <-- This is the crucial base case check
            # Print the current node with indentation
            print(' ' * (5 * level) + prefix + str(node.value))
            # Only print child branches if the current node has children
            if node.left or node.right:
                 # Recursively print the left child (if it exists)
                 # Using 'L----' prefix and incrementing level
                 self.print_tree(node.left, level + 1, 'L----')
                 # Recursively print the right child (if it exists)
                 # Using 'R----' prefix and incrementing level
                 self.print_tree(node.right, level + 1, 'R----')
            else:
                print(' ' * (5 * (level + 1)) + 'None'


#-----------------------------------------------------#
#            COMMAND LINE INTERFACE                   #
#-----------------------------------------------------#              
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
'''
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
'''
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

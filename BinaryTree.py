# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------

# Create a test tree:
#         A
#        / \
#       B   C
#      / \   \
#     D  E    F
#
# Print BST with indentation
# Print the nodes pre-order, in-order, post-order           
#------------------------------------------------  

from TreeNode import Node
from io import StringIO
import sys


# --- BinaryTree Class ---
# Represents a AVL Tree, implement common traversal methods and print_tree().
class BinaryTree:
    def __init__(self, root=None):
        """
        Initializes a BinaryTree with an optional root node.

        Args:
            root: The root node of the binary tree.
        """
        self.root = root # The root node of the tree

    def inorder(self, node=None):
        """
        Performs an in-order traversal of the binary tree.
        Visits nodes in the order: left subtree, root, right subtree.

        Args:
            node: The current node being traversed.
        """
        if node:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def preorder(self, node=None):
        """
        Performs a pre-order traversal of the binary tree.
        Visits nodes in the order: root, left subtree, right subtree.

        Args:
            node: The current node being traversed.
        """
        if node: # If the current node is not None
            print(node.value, end=' ')      # Visit (print) the current node's value
            self.preorder(node.left)        # Recursively traverse the left subtree
            self.preorder(node.right)       # Recursively traverse the right subtree

    def postorder(self, node=None):
        """
        Performs a post-order traversal of the binary tree.
        Visits nodes in the order: left subtree, right subtree, root.

        Args:
            node: The current node being traversed. Defaults to the root of the tree.
        """
        if node: # If the current node is not None
            self.postorder(node.left)       # Recursively traverse the left subtree
            self.postorder(node.right)      # Recursively traverse the right subtree
            print(node.value, end=' ')      # Visit (print) the current node's value

    def print_tree(self, node=None, level=0, prefix='Root:'):
        """
        Prints the binary tree in a visually appealing format.

        Args:
            node: The starting node for printing. Defaults to the root of the tree.
            level: The current level of the tree. Defaults to 0 (used for indentation).
            prefix: The prefix for indiicate the position of the node (e.g. "Root:", "L----", "R----").
        """
        if node: # If the current node is None
            print(' ' * (5 * level) + prefix + str(node.value)) # Print the node's value with indentation
            if node.left or node.right:  # If the node has children
                # Recursively call print_tree on left and right children
                self.print_tree(node.left, level + 1, 'L----')
                self.print_tree(node.right, level + 1, 'R----')


# --- Command Line Interface ---
# Demonstrate the structure of a sample Binary Tree
# Command Line Interface
# Create a test tree:
#         A
#        / \
#       B   C
#      / \   \
#     D  E    F


if __name__ == "__main__":
    print("--- Running Example Usage ---")

    bt = BinaryTree()
    bt.root = Node('A')
    bt.root.left = Node('B')
    bt.root.right = Node('C')
    bt.root.left.left = Node('D')
    bt.root.left.right = Node('E')
    bt.root.right.right = Node('F')

    print("\n\nPrint The Sample Binary Tree")
    bt.print_tree(bt.root)

    print("\n\nIn-order Traversal:")
    bt.inorder(bt.root)
    print("\n\nPre-order Traversal:")
    bt.preorder(bt.root)
    print("\n\nPost-order Traversal:")
    bt.postorder(bt.root)

from io import StringIO
import sys
from TreeNode import Node
from BinaryTree import BinaryTree
from BST import BST


# --- AVLTree Class ---
# Represents a AVL Tree, inheriting basic tree operations from BST.
class AVLTree(BST):
    def __init__(self, root=None):
        """
        Initializes an AVL Tree with an optional root node.

        Args:
            root: The root node of the AVL tree.
        """
        super().__init__(root)    # Inherit from BST


    def get_height(self, node):
        """
        Gets the height of a node in the AVL tree.

        Args:
            node: The node to get the height of.

        Returns:
            int: The height of the node.
        """
        if not node:          # If the node is None
            return -1         # Conventionally -1 for a null node, 0 for a leaf
        return node.height    # Otherwise, return the node's height

    def get_balance(self, node):
        """
        Gets the balance factor of a node in the AVL tree.

        Args:
            node: The node to get the balance factor of.

        Returns:
            int: The balance factor of the node.
        """
        if not node:          # If the node is None
            return 0.         # Balance factor is 0 for a null node (leaf node)
        return self.get_height(node.left) - self.get_height(node.right) # Calculate balance factor

    def left_rotate(self, z):
        """
        Performs a left rotation on a node in the AVL tree.

        Args:
            z: The node to rotate.

        Returns:
            Node: The new root of the rotated subtree.
        """
        # Initialize the nodes needed
        y = z.right
        T2 = y.left

        # Rotate
        y.left = z
        z.right = T2

        # Update heights AFTER rotation
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y   # Return the new root of the subtree (y)

    def right_rotate(self, z):
        """
        Performs a right rotation on a node in the AVL tree.

        Args:
            z: The node to rotate.

        Returns:
            Node: The new root of the rotated subtree.
        """
        # Initialize the nodes needed
        y = z.left
        T3 = y.right

        # Rotate
        y.right = z
        z.left = T3

        # Update heights AFTER rotation
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y   # Return the new root of the subtree (y)

    # Override insert from BST
    def insert(self, value):
        """
        Inserts a value into the AVL Tree, maintaining the AVL property.

        Args:
            value: The value to insert.
        """
        def _insert(node, value):
            """
            Recursive helper for insertion.

            Args:
                node: The current node being examined.
                value: The value to insert.

            Returns:
                Node: The root of the subtree after insertion.
            """
            # Standard BST insertion
            if not node:   # If the current node is None (empty subree)
                return Node(value)    # Create a new node with the value and return it
            if value < node.value:    # If the value is less than the current node's value
                node.left = _insert(node.left, value) # Insert into the left subtree
            elif value > node.value:  # If the value is greater than the current node's value
                node.right = _insert(node.right, value) # Insert into the right subtree
            else:
                print(f"Duplicated key {value} ignored.") # Suppress during insertion if not testing output
                return node # Value already exists, return the current node

            # Update height of current node after insertion into subtree
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

            # Get balance factor
            balance = self.get_balance(node)

            # Perform rotations if unbalanced
            # ----------------------------------
            # Left Left Case
            if balance > 1 and value < node.left.value:
                return self.right_rotate(node)

            # Right Right Case
            if balance < -1 and value > node.right.value:
                return self.left_rotate(node)

            # Left Right Case
            if balance > 1 and value > node.left.value:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

            # Right Left Case
            if balance < -1 and value < node.right.value:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

            # Return the (potentially new) root of the subtree
            return node

        self.root = _insert(self.root, value)  # Start the insertion from the root


    # Override print_tree from BinaryTree to include balance factor (already done)
    def print_tree(self, node=None, level=0, prefix='Root:'):
        """
        Prints the AVL tree in a visually appealing format.

        Args:
            node: The starting node for printing. Defaults to the root of the tree.
            level: The current level of the tree. Defaults to 0 (used for indentation).
            prefix: The prefix for indiicate the position of the node (e.g. "Root:", "L----", "R----").
        """
        # Ensure get_balance is called on the correct object (self)
        if node:    # If the current node is not None
            balance = self.get_balance(node)  # Get the balance factor of the node
            print(' ' * (5 * level) + prefix + f"{node.value} (BF={balance})") # Print node value and balance factor
            # Recursively call print_tree on left and right, passing self
            self.print_tree(node.left, level + 1, 'L----') # Print left subtree
            self.print_tree(node.right, level + 1, 'R----') # Print right subtree



 # --- Command Line Interface ---
 #---------------------------------------------------------
 # Demo of AVL: insert() with balance factor (BF)
 #---------------------------------------------------------
 #      50
 #    /   \
 #   30    70
 #  /  \   /  \
 # 20  40 60  80

    print("\n\n-------Demo of AVL: insert() with balance factor-------")
    avl = AVLTree()

    # Insert node(50) into the AVL tree
    print("\n\nInsert node(50) into the AVL tree")
    avl.insert(50)
    print()
    avl.print_tree(avl.root)
    print() # Add a newline after traversal output

    print("\n\nInsert node(30) into the AVL tree")
    avl.insert(30)
    print()
    avl.print_tree(avl.root)
    print() # Add a newline after traversal output

    print("\n\nInsert node(70) into the AVL tree")
    avl.insert(70)
    print()
    avl.print_tree(avl.root)
    print() # Add a newline after traversal output

    print("\n\nInsert node(20) into the AVL tree")
    avl.insert(20)
    print()
    avl.print_tree(avl.root)
    print() # Add a newline after traversal output

    print("\n\nInsert node(40) into the AVL tree")
    avl.insert(40)
    print()
    avl.print_tree(avl.root)
    print() # Add a newline after traversal output

    print("\n\nInsert node(60) into the AVL tree")
    avl.insert(60)
    print()
    avl.print_tree(avl.root)
    print() # Add a newline after traversal output

    print("\n\nInsert node(80) into the AVL tree")
    avl.insert(80)
    print()
    avl.print_tree(avl.root)
    print() # Add a newline after traversal output
    print("\n------The end of Sample AVL Tree--------")

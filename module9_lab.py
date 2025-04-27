
# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------
# import unittest
import sys
from io import StringIO # Used for capturing print output in tests


# --- Class Definitions ---
#--------------------------

# --- Node Class ---
# Represents a tree Node, with value, left, right and height member datas.
class Node:
    def __init__(self, value=None):
        self.value = value      # Store data in the node
        self.left = None        # Pointer to the left child node
        self.right = None       # Pointer to the right child node
        self.height = 0         # Height of the node (used in AVL trees for balancing)

    def __str__(self):
        # Return a string representation of the node's value
        return str(self.value)


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


# --- BST Class ---
# Represents a BST, inheriting basic tree operations from BinaryTree.
class BST(BinaryTree):
    def __init__(self, root=None):
        """
        Initializes a BST with an optional root node.

        Args:
            root: The root node of the binary search tree.
        """
        super().__init__(root)


    def insert(self, value):
        """
        Inserts a value into the Binary Search Tree.

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
            if not node: # If the current node is None (empty subtree)
                return Node(value)  # Create a new node with the value and return it
            if value < node.value:  # If the value is less than the current node's value
                node.left = _insert(node.left, value)  # Recursively insert into the left subtree
            elif value > node.value:  # If the value is greater than the current node's value
                node.right = _insert(node.right, value)  # Recursively insert into the right subtree
            else:
                print(f"Duplicated key {value} ignored.") # Suppress this during test setup unless testing output
                pass # Or handle differently if testing this specific output
            return node # Return the current node (potentially modified)

        self.root = _insert(self.root, value) # Start the insertion from the root


    def search(self, value):
        """
        Searches for a value in the Binary Search Tree using recursion.

        Args:
            value: The value to search for.

        Returns:
            Node: The node containing the value if found, otherwise None.
        """
        def _search(node, value):
            """
            Recursive helper for searching a value.

            Args:
                node: The current node being examined in the recursion.
                value: The value to search for.

            Returns:
                Node: The node if found, otherwise None.
            """
            # Base Case 1: If the current node is None, the value was not found
            # along this path. Return None.
            # Base Case 2: If the current node's value matches the search value,
            # we found the node. Return the node.
            if node is None or value == node.value:
                print(f"DEBUG: Search returning {node.value if node else 'None'}") # Debug statement (handle node being None)
                return node # Return the node if found, or None if node is None

            # Recursive Step: Compare the search value with the current node's value.
            if value < node.value:
                # If the search value is smaller, the target node must be in the left subtree.
                # Recursively call _search on the left child.
                print(f"DEBUG: Search going left from {node.value}") # Debug statement
                return _search(node.left, value)
            else: # value > node.value
                # If the search value is larger, the target node must be in the right subtree.
                # Recursively call _search on the right child.
                print(f"DEBUG: Search going right from {node.value}") # Debug statement
                return _search(node.right, value)

        # Start the recursive search from the root of the tree.
        return _search(self.root, value)

    # Remove a value from the BST (recursive implementation)
    def remove(self, value):
        """
        Removes a value from the Binary Search Tree using recursion.

        Args:
            value: The value to remove.
        """
        # --- Helper Method: Find Minimum Value Node ---
        # Used to find the inorder successor for deletion Case 3.
        def _min_value_node(node):
            """
            Finds the node with the minimum value in the subtree rooted at 'node'.
            This is used to find the inorder successor in deletion.

            Args:
                node: The root of the subtree to search within.

            Returns:
                Node: The node containing the minimum value in the subtree, or None
                      if the input node is None or the subtree is empty.
            """
            # Start from the given node
            current = node
            # Keep traversing left until the leftmost node is found
            # The leftmost node in a subtree is the one with the minimum value.
            while current and current.left: # Added check for 'current' being not None
                current = current.left
            # Return the node found (which might be None if the input node was None)
            return current

        # Define the recursive helper function _remove
        # It takes the current node and the value to remove,
        # and returns the root of the (potentially modified) subtree.
        def _remove(node, value):
            """
            Recursive helper for removal.

            Args:
                node: The current node being examined.
                value: The value to remove.

            Returns:
                Node: The root of the subtree after removal.
            """
            # Base Case 1: If the current node is None, the value was not found
            # in this branch of the tree. Return None.
            if node is None: # if not node:
                print(f"DEBUG: Value {value} not found in this branch.") # Debug statement
                return node # Return node (which is None)

            # Recursive Step 1: Navigate down the tree to find the node to remove.
            if value < node.value:
                # If the value is smaller, the node to remove is in the left subtree.
                # Recursively call _remove on the left child and assign the result
                # back to node.left. This re-links the parent.
                print(f"DEBUG: Going left from {node.value}") # Debug statement
                node.left = _remove(node.left, value)
            elif value > node.value:
                # If the value is larger, the node to remove is in the right subtree.
                # Recursively call _remove on the right child and assign the result
                # back to node.right. This re-links the parent.
                print(f"DEBUG: Going right from {node.value}") # Debug statement
                node.right = _remove(node.right, value)
            else:
                # Node Found! The current 'node' is the one to be removed.
                # Now handle the three deletion cases:

                # Case 1: Node has 0 or 1 child.
                # If no left child, the right child (or None) replaces this node.
                if not node.left:
                    print(f"DEBUG: Case 1/2a - No left child.") # Debug statement
                    # Return the right child. The parent's pointer will be updated to this.
                    return node.right
                # If no right child (but has a left), the left child replaces this node.
                # This is effectively Case 2b.
                if not node.right: # Checks if node.right is None
                    print(f"DEBUG: Case 1/2b - No right child.") # Debug statement
                    # Return the left child. The parent's pointer will be updated to this.
                    return node.left

                # Case 3: Node has two children.
                # print(f"DEBUG: Case 3 - Two children.") # Debug statement
                # Find the inorder successor: the smallest node in the right subtree.
                # This node has a value greater than node.value but is the smallest
                # such value, making it suitable to replace the removed node while
                # maintaining the BST property.
                min_node = _min_value_node(node.right)
                print(f"DEBUG: Successor is {min_node.value}") # Debug statement

                # Copy the value of the inorder successor to the current node (the one we want to remove).
                # Conceptually, the current node is replaced by the successor's value.
                node.value = min_node.value # Note: Original code used node.key, changed to node.value for consistency

                # Now, recursively remove the inorder successor from the right subtree.
                # The successor is guaranteed to have at most one right child, so
                # the recursive call will eventually hit Case 1 or Case 2.
                # Assign the result back to node.right to update the right subtree.
                print(f"DEBUG: Recursively removing successor {min_node.value} from right subtree.") # Debug statement
                node.right = _remove(node.right, min_node.value)

            # Return the current node. This is essential for the recursive calls
            # to re-link the parent's pointer to this node or its modified subtree.
            return node

        # Start the recursive removal process from the root.
        # The result of the recursive call (the potentially new root of the entire tree)
        # is assigned back to self.root. This handles the case where the root node
        # itself is removed.
        self.root = _remove(self.root, value)


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
# Demonstrate the structure of a sample Binary Tree
# Demonstrate the structure of a sample BST
# Demonstrate the structure of a sample AVL Tree with balance factor (BF)
if __name__ == "__main__":
    print("--- Running Example Usage ---")

 #----------------------------------------------------
 # Demo of BinaryTree (travesal methods, print_tree())
 #----------------------------------------------------
    print("\n\n------Demo of BinaryTree (travesal methods, print_tree())------")

    bt = BinaryTree()
    bt.root = Node('A')
    bt.root.left = Node('B')
    bt.root.right = Node('C')
    bt.root.left.left = Node('D')
    bt.root.left.right = Node('E')
    bt.root.right.right = Node('F')

    print("\n\nPrint The Sample Binary Tree")
    print()
    bt.print_tree(bt.root)

    print("\n\nIn-order Traversal:")
    bt.inorder(bt.root)
    print("\n\nPre-order Traversal:")
    bt.preorder(bt.root)
    print("\n\nPost-order Traversal:")
    bt.postorder(bt.root)
    print("\n\n------The end of Demo of Sample Binary Tree------")
    print("---------------------------------------------------")
 # ------------The End of Demo of BinaryTree---------------


 #---------------------------------------------------------
 # Demo of BST: insert(), search(), remove(), inorder()
 #---------------------------------------------------------
 #      50
 #    /   \
 #   30    70
 #  /  \   /  \
 # 20  40 60  80

    print("\n\n-------Demo of BST: insert(), search(), remove(), inorder()------")
    bst = BST()
    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        print(f"\nInserting value: {value}")
        bst.insert(value)

    print("\n\nPrint the sample BST tree")
    print()
    bst.print_tree(bst.root)

    print("\n\nIn-order Traversal through the sample BST tree:")
    print()
    bst.inorder(bst.root)
    print() # Add a newline after traversal output

    print("\n\nPre-order Traversal through the sample BST tree:")
    print()
    bst.preorder(bst.root)
    print() # Add a newline after traversal output

    print("\n\nPost-order Traversal through the sample BST tree:")
    print()
    bst.postorder(bst.root)
    print() # Add a newline after traversal output


    print("\n\nSearch for 40 in the sample BST:")
    print()
    found_node = bst.search(40)
    if found_node:
        print(f"Found node with value: 40")
    else:
        print(f"Value 40 not found.")

    print("\n\nSearch for 100 in the sample BST: ")
    print()
    found_node = bst.search(100)
    if found_node:
        print(f"Found node with value: 100")
    else:
        print(f"Value 100 not found.")

    print("\n\nSearch for 60 in the sample BST: ")
    print()
    found_node = bst.search(60)
    if found_node:
        print(f"Found node with value: 60")
    else:
        print(f"Value 60 not found.")

    # Remove leaf node 20 (with no child)
    print("\n\nRemove leaf node 20 from the sample BST:")
    print()
    bst.remove(20)
    print("\n\nIn-order Traversal after node 20 removed:")
    bst.inorder(bst.root)
    print("\n\n")
    bst.print_tree(bst.root)

    # Remove node 30 (only with right child Node(40))
    print("\n\nRemove node 30 from the sample BST:")
    print()
    bst.remove(30)
    print("\n\nIn-order Traversal after node 30 removed:")
    bst.inorder(bst.root)
    print("\n\n")
    bst.print_tree(bst.root)


    # Remove node 50 (with two children)
    print("\n\nRemove node 50 from the sample BST:")
    print()
    bst.remove(50)
    print("\n\nIn-order Traversal after node 50 removed")
    bst.inorder(bst.root)
    print("\n\n")
    bst.print_tree(bst.root)
    print("\n\n------The End of Demo of BST sample tree-------")
    print("-------------------------------------------------")
 # ------------The End of Demo of BST---------------

 #---------------------------------------------------------
 # Demo of AVL: insert() with balance factor
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





'''

# --- Helper function to capture print output ---
# Useful for unit testing methods that print to stdout.
def capture_print_output(func, *args, **kwargs):
    """
    Captures the standard output (stdout) produced by a function call.

    Args:
        func: The function to call.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        str: The captured output as a string.
    """
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        # Call the function with provided arguments
        func(*args, **kwargs)
    finally:
        # Restore standard output regardless of exceptions
        sys.stdout = old_stdout
    # Return the value captured in the StringIO buffer
    return captured_output.getvalue()


# --- Unit Tests ---
# ------------------
class TestBST(unittest.TestCase):
    # setUp is called before each test method (test_*)
    def setUp(self):
        # Initialize an empty BST for each test case
        self.bst = BST()
        # Define a standard set of keys/values to build a base tree
        self.values = [10, 5, 15, 2, 7, 12, 20]
        # Define a value not in the standard set for negative search tests
        self.non_existent_value = 99

    # Helper to build the standard tree using the current insert method (recursive)
    def build_base_tree(self):
         """Builds the standard base tree using the BST's insert method."""
         print("Building base tree with values:", self.values)
         for value in self.values:
            self.bst.insert(value)

    # Test case for inserting values and verifying the structure
    def test_insert(self):
        print("\nTesting Insert:")
        # Build the base tree using the insert method (which is recursive)
        self.build_base_tree()

        # Verify the base structure built
        print("Verifying base tree structure after insertion...")
        self.assertIsNotNone(self.bst.root, "Tree root should not be None after insertion")
        self.assertEqual(self.bst.root.value, 10)
        self.assertEqual(self.bst.root.left.value, 5)
        self.assertEqual(self.bst.root.right.value, 15)
        self.assertEqual(self.bst.root.left.left.value, 2)
        self.assertEqual(self.bst.root.left.right.value, 7)
        self.assertEqual(self.bst.root.right.left.value, 12)
        self.assertEqual(self.bst.root.right.right.value, 20)

        # Test inserting a new value (8) and verify its position
        # Based on BST rules, 8 goes to the right of 7 (10 -> 5 -> 7 -> 8)
        print("Inserting 8...")
        self.bst.insert(8)

        # Assert that the node exists before checking its value
        self.assertIsNotNone(self.bst.root.left.right, "Node 7 should exist")
        self.assertIsNotNone(self.bst.root.left.right.right, "Node 8 should be inserted as the right child of 7")
        # Now check the value
        self.assertEqual(self.bst.root.left.right.right.value, 8)
        # Also assert that the node that was *not* inserted there is still None
        self.assertIsNone(self.bst.root.left.right.left, "Left child of 7 should still be None after inserting 8")

        # Test inserting a duplicate value
        print("Testing duplicate insertion (inserting 5 again)...")
        # Capture stdout to check the printed message
        output = capture_print_output(self.bst.insert, 5)
        self.assertIn("Duplicated key 5 ignored.", output)


    # Test case for searching values using the recursive search
    def test_search(self):
        print("\nTesting Search (Recursive):")
        # Build the tree to search within
        self.build_base_tree()
        print("Built base tree for search.")

        # Test searching for values that ARE in the tree
        print("Searching for values that should be found...")
        for value in self.values:
            found_node = self.bst.search(value)
            self.assertIsNotNone(found_node, f"Value {value} should be found")
            self.assertEqual(found_node.value, value, f"Found node value should match {value}")

        # Test searching for a value that is NOT in the tree
        print(f"Searching for non-existent value {self.non_existent_value}...")
        not_found_node = self.bst.search(self.non_existent_value)
        self.assertIsNone(not_found_node, f"Value {self.non_existent_value} should not be found")

    # Test cases for removing values using the recursive remove
    def test_remove_leaf(self):
        print("\nTesting Remove (Leaf, Recursive):")
        self.build_base_tree()
        print("Before removing 2 (leaf node):")
        # self.bst.print_tree() # Optional: visualize
        self.assertIsNotNone(self.bst.search(2), "Value 2 should exist before removal")
        self.bst.remove(2)
        print("After removing 2:")
        # self.bst.print_tree() # Optional: visualize

        # Verify the node is removed using search
        self.assertIsNone(self.bst.search(2), "Value 2 should be removed")
        # Verify the parent's pointer is updated
        self.assertIsNone(self.bst.root.left.left, "5's left child should be None after removing 2")
        self.assertIsNotNone(self.bst.root.left, "Node 5 should still exist (parent of removed node)")

    def test_remove_node_with_one_child(self):
        print("\nTesting Remove (Node with One Child, Recursive):")
        self.build_base_tree()
        # Insert a node (13) to make 12 a node with one child (13).
        print("Inserting 13 to set up one-child removal case (removing 12)...")
        self.bst.insert(13) # 10 -> 15 -> 12 -> 13 (right child)
        self.assertIsNotNone(self.bst.search(13), "Value 13 should be inserted")

        print("Before removing 12 (node with right child 13):")
        # self.bst.print_tree() # Optional: visualize
        self.assertIsNotNone(self.bst.search(12), "Value 12 should exist before removal")
        self.assertIsNotNone(self.bst.search(13), "Value 13 should exist")

        self.bst.remove(12)
        print("After removing 12:")
        # self.bst.print_tree() # Optional: visualize

        self.assertIsNone(self.bst.search(12), "Value 12 should be removed (node with one child)")
        # Check that 15's left child is now 13 (12's only child)
        self.assertIsNotNone(self.bst.root.right, "Node 15 should still exist (parent)")
        self.assertIsNotNone(self.bst.root.right.left, "15's left child should not be None")
        self.assertEqual(self.bst.root.right.left.value, 13, "15's left child should now be 13")


    def test_remove_node_with_two_children(self):
        print("\nTesting Remove (Two Children, Recursive):")
        self.build_base_tree()
        print("Before removing 10 (root node with two children):")
        # self.bst.print_tree() # Optional: visualize
        self.assertIsNotNone(self.bst.search(10), "Value 10 should exist before removal")
        # The inorder successor of 10 is the minimum in its right subtree (15 -> 12). So the successor is 12.
        self.assertIsNotNone(self.bst.search(12), "Successor 12 should exist")

        self.bst.remove(10)
        print("After removing 10:")
        # self.bst.print_tree() # Optional: visualize

        self.assertIsNone(self.bst.search(10), "Value 10 should be removed")
        # Check that the root is now the successor (12)
        self.assertEqual(self.bst.root.value, 12, "Root should be updated to 12")
        # Check that 15's left child (which was 12) is now None, because 12 was moved up
        self.assertIsNotNone(self.bst.root.right, "Node 15 should still exist (parent of successor location)")
        self.assertIsNone(self.bst.root.right.left, "15's left child should be None after 12 was moved")


    def test_remove_non_existent(self):
        print("\nTesting Remove (Non-existent Value, Recursive):")
        self.build_base_tree()
        self.bst.remove(self.non_existent_value)
        self.assertIsNone(self.bst.search(self.non_existent_value), "Non-existent value should not be found")
        # Ensure the tree structure didn't change (e.g., root is still 10)
        self.assertEqual(self.bst.root.value, 10, "Root should remain unchanged when removing non-existent value")

# Running Unit Test
# ---------------------
if __name__ == "__main__":

    # --- Running Unit Tests ---
    print("\n\n--- Running Unit Tests ---")
    # Note: argv and exit=False are used so that unittest.main() doesn't
    # try to parse command-line arguments or exit the script immediately.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------


# Create a test tree manually                                
#          50                                                  
#        /    \                                                 
#       30     70                                                
#     /   \   /   \                                               
#    20   40  60   80                                            
# 
# Print BST with indentation
# Print the nodes pre-order, in-order, post-order           
# ######################################################   
import unittest
from TreeNode import Node
from BinaryTree import BinaryTree


# --- BST Class ---
# Represents a Binary Search Tree, inheriting basic tree operations.
class BST(BinaryTree):
    # Constructor for the BST class
    def __init__(self, root=None):
        """
        Initializes a Binary Search Tree.

        Args:
            root: The root node of the BST. Defaults to None (empty BST).
        """
        super().__init__(root) # Call the parent BinaryTree constructor


    # Insert a value into the BST (recursive implementation)
    def insert(self, value):
        """
        Inserts a new value into the Binary Search Tree using recursion.

        Args:
            value: The value to insert.
        """
        # Define the recursive helper function _insert
        # It takes the current node and the value to insert,
        # and returns the root of the (potentially new) subtree.
        def _insert(node, value):
            """
            Recursive helper for insertion.

            Args:
                node: The current node being examined.
                value: The value to insert.

            Returns:
                Node: The root of the subtree after insertion.
            """
            # Base case: If the current node is None, we found the correct spot
            # to insert the new node. Create it and return it.
            if not node: # Equivalent to node is None
                # print(f"DEBUG: Creating node with value {value}") # Debug statement
                return Node(value)

            # Recursive step: Compare the value with the current node's value.
            if value < node.value:
                # If the value is smaller, go to the left subtree.
                # The recursive call returns the root of the modified left subtree,
                # which we then assign back to node.left.
                # print(f"DEBUG: Going left from {node.value}") # Debug statement
                node.left = _insert(node.left, value)
            elif value > node.value:
                # If the value is larger, go to the right subtree.
                # The recursive call returns the root of the modified right subtree,
                # which we then assign back to node.right.
                # print(f"DEBUG: Going right from {node.value}") # Debug statement
                node.right = _insert(node.right, value)
            else:
                # If the value is equal, it's a duplicate. Do nothing and print a message.
                # Return the current node as the subtree remains unchanged.
                print(f"Duplicated key {value} ignored.")
                return node # Explicitly return the node

            # Return the current node. This is crucial in the recursive approach
            # as it re-links the parent node's pointer to this (potentially modified)
            # node or the new node created in the base case.
            return node

        # Start the recursive insertion from the root.
        # The result of the recursive call (the potentially new root of the entire tree)
        # is assigned back to self.root. This handles insertion into an empty tree
        # as well as inserting into non-empty trees.
        self.root = _insert(self.root, value)


    # Search for a value in the BST (recursive implementation)
    def search(self, value):
        """
        Searches for a value in the Binary Search Tree using recursion.

        Args:
            value: The value to search for.

        Returns:
            Node: The node containing the value if found, otherwise None.
        """
        # Define the recursive helper function _search
        # It takes the current node (starting point) and the value to search for.
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
            # --- FIX: Use 'value' consistently instead of 'key', fix debug print ---
            if node is None or value == node.value:
                # print(f"DEBUG: Search returning {node.value if node else 'None'}") # Debug statement (handle node being None)
                return node # Return the node if found, or None if node is None

            # Recursive Step: Compare the search value with the current node's value.
            if value < node.value:
                # If the search value is smaller, the target node must be in the left subtree.
                # Recursively call _search on the left child.
                # print(f"DEBUG: Search going left from {node.value}") # Debug statement
                return _search(node.left, value)
            else: # value > node.value
                # If the search value is larger, the target node must be in the right subtree.
                # Recursively call _search on the right child.
                # print(f"DEBUG: Search going right from {node.value}") # Debug statement
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
                # print(f"DEBUG: Value {value} not found in this branch.") # Debug statement
                return node # Return node (which is None)

            # Recursive Step 1: Navigate down the tree to find the node to remove.
            if value < node.value:
                # If the value is smaller, the node to remove is in the left subtree.
                # Recursively call _remove on the left child and assign the result
                # back to node.left. This re-links the parent.
                # print(f"DEBUG: Going left from {node.value}") # Debug statement
                node.left = _remove(node.left, value)
            elif value > node.value:
                # If the value is larger, the node to remove is in the right subtree.
                # Recursively call _remove on the right child and assign the result
                # back to node.right. This re-links the parent.
                # print(f"DEBUG: Going right from {node.value}") # Debug statement
                node.right = _remove(node.right, value)
            else:
                # Node Found! The current 'node' is the one to be removed.
                # Now handle the three deletion cases:

                # Case 1: Node has 0 or 1 child.
                # If no left child, the right child (or None) replaces this node.
                if not node.left:
                    # print(f"DEBUG: Case 1/2a - No left child.") # Debug statement
                    # Return the right child. The parent's pointer will be updated to this.
                    return node.right
                # If no right child (but has a left), the left child replaces this node.
                # This is effectively Case 2b.
                if not node.right: # Checks if node.right is None
                    # print(f"DEBUG: Case 1/2b - No right child.") # Debug statement
                    # Return the left child. The parent's pointer will be updated to this.
                    return node.left

                # Case 3: Node has two children.
                # print(f"DEBUG: Case 3 - Two children.") # Debug statement
                # Find the inorder successor: the smallest node in the right subtree.
                # This node has a value greater than node.value but is the smallest
                # such value, making it suitable to replace the removed node while
                # maintaining the BST property.
                min_node = _min_value_node(node.right)
                # print(f"DEBUG: Successor is {min_node.value}") # Debug statement

                # Copy the value of the inorder successor to the current node (the one we want to remove).
                # Conceptually, the current node is replaced by the successor's value.
                node.value = min_node.value # Note: Original code used node.key, changed to node.value for consistency

                # Now, recursively remove the inorder successor from the right subtree.
                # The successor is guaranteed to have at most one right child, so
                # the recursive call will eventually hit Case 1 or Case 2.
                # Assign the result back to node.right to update the right subtree.
                # print(f"DEBUG: Recursively removing successor {min_node.value} from right subtree.") # Debug statement
                node.right = _remove(node.right, min_node.value)

            # Return the current node. This is essential for the recursive calls
            # to re-link the parent's pointer to this node or its modified subtree.
            return node

        # Start the recursive removal process from the root.
        # The result of the recursive call (the potentially new root of the entire tree)
        # is assigned back to self.root. This handles the case where the root node
        # itself is removed.
        self.root = _remove(self.root, value)

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


# --- BST Tests ---
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


# --- Command Line Interface ---
# Demonstrate the structure of a sample Binary Tree
# Demonstrate the structure of a sample BST
# Demonstrate the structure of a sample AVL Tree with balance factor (BF)

if __name__ == "__main__":
    # Control whether to run demos or unit tests
    run_tests = False  # <-- Set to True if you want to run unit tests
    if not run_tests:
        print("--- Running Example Usage ---")


        # Demo of BST: insert(), search(), remove(), inorder()
        #-------------------------------------------------
        #      50
        #    /   \
        #   30    70
        #  /  \   /  \
        # 20  40 60  80

        # DEMO: BST
        print("\n\n------- Demo of BST: insert(), search(), remove(), traversal ------")
        bst = BST()
        values = [50, 30, 70, 20, 40, 60, 80]
        for value in values:
            print(f"\nInserting value: {value}")
            bst.insert(value)

        print("\nPrint the Sample BST:")
        bst.print_tree(bst.root)

        print("\nIn-order Traversal:")
        bst.inorder(bst.root)

        print("\n\nPre-order Traversal:")
        bst.preorder(bst.root)

        print("\n\nPost-order Traversal:")
        bst.postorder(bst.root)

        print("\n\nSearching values in BST:")
        search_values = [40, 100, 60]
        for value in search_values:
            found = bst.search(value)
            print(f"\nSearch for {value}: {'Found' if found else 'Not Found'}")

        print("\n\nRemoving values from BST:")
        for remove_value in [20, 30, 50]:
            print(f"\nRemoving {remove_value}:")
            bst.remove(remove_value)
            print("\nBST after removal:")
            bst.print_tree(bst.root)
           # ------------The End of Demo of BST---------------
    else:
        print("--- Running Unit Tests ---\n")
        unittest.main(argv=['first-arg-is-ignored'], exit=False)

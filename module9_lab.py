
# Group Members: Michael Jung (ID:10680322), Timothy Sanders (??), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------
import unittest
import sys
from io import StringIO # Used for capturing print output in tests
from TreeNode import Node
from BinaryTree import BinaryTree
import BST



# --- Node Class ---
# Represents a single node in the binary tree or BST.
class Node:
    # Constructor for the Node class
    def __init__(self, value=None):
        """
        Initializes a new node with a given value.

        Args:
            value: The data to be stored in the node. Defaults to None.
        """
        self.value = value
        self.left = None  # Pointer to the left child node
        self.right = None # Pointer to the right child node

    # String representation of the Node
    def __str__(self):
        """
        Returns the string representation of the node's value.
        """
        return str(self.value)


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
            self.inorder(node.left) # Recurse on left child
            print(node.value, end=' ')  # Visit the current node (print its value)
            self.inorder(node.right) # Recurse on right child

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


if __name__ == "__main__":

 #----------------------------------------------------
 # Demo of BinaryTree (travesal methods, print_tree()) 
 #----------------------------------------------------
    bt = BinaryTree() # Instantiate an object of BinaryTree
    bt.root = Node('A')
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
# ------------The End of Demo of BinaryTree---------------



 #---------------------------------------------------------
 # Demo of BST: insert(), search(), remove(), inorder() 
 #---------------------------------------------------------
    bst = BST()

    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        bst.insert(key)


    print("\n\nPrint Binary Search Tree")
    bst.print_tree(bst.root)

    print("\n\nPre-order Traversal through the BST:")
    bst.preorder(bst.root)

    print("\n\nIn-order Traversal through the BST:")
    bst.inorder(bst.root)

    print("\n\nPost-order Traversal through the BST:")
    bst.postorder(bst.root)

    print("\n\nSearch for 40:")
    print(bst.search(40))

    print("\n\nSearch for 100:")
    print(bst.search(100))

    print("\n\nSearch for 60:")
    print(bst.search(60))

    print("\n\nRemove 20:")
    bst.remove(20)
    bst.print_tree(bst.root)
    bst.inorder(bst.root)


    print("\n\nRemove 30:")
    bst.remove(30)
    bst.print_tree(bst.root)
    bst.inorder(bst.root)


    print("\n\nRemove 50:")
    bst.remove(50)
    bst.print_tree(bst.root)
    bst.inorder(bst.root)
# ------------The End of Demo of BST---------------









'''
# --- Unit Tests ---
#--------------------
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

# --- Example Usage (Original Main Block) ---
if __name__ == "__main__":
    print("--- Running Example Usage ---")
    bst = BST()

    values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting values: {values}")
    for value in values:
        bst.insert(value)

    print("\n\nPrint Binary Search Tree Structure:")
    bst.print_tree(bst.root)

    print("\n\nPre-order Traversal through the BST:")
    bst.preorder(bst.root)
    print() # Add a newline after traversal output

    print("\n\nIn-order Traversal through the BST:")
    bst.inorder(bst.root)
    print() # Add a newline after traversal output

    print("\n\nPost-order Traversal through the BST:")
    bst.postorder(bst.root)
    print() # Add a newline after traversal output

    search_value_found = 40
    print(f"\n\nSearch for {search_value_found}:")
    found_node = bst.search(search_value_found)
    if found_node:
        print(f"Found node with value: {found_node.value}")
    else:
        print(f"Value {search_value_found} not found.")


    search_value_not_found = 100
    print(f"\n\nSearch for {search_value_not_found}:")
    found_node = bst.search(search_value_not_found)
    if found_node:
        print(f"Found node with value: {found_node.value}")
    else:
        print(f"Value {search_value_not_found} not found.")

    insert_value = 100
    print(f"\n\nInsert {insert_value}:")
    bst.insert(insert_value)
    print(f"Tree after inserting {insert_value}:")
    bst.print_tree(bst.root)

    # Note: 20 is now a leaf again after inserting 100, 70, etc.
    remove_value_leaf = 20
    print(f"\n\nRemove {remove_value_leaf} (leaf):")
    bst.remove(remove_value_leaf)
    print(f"Tree after removing {remove_value_leaf}:")
    bst.print_tree(bst.root)

    # 70 has a right child 80 and its left child (60) after inserting 100.
    # In the tree [50, 30, 70, 20, 40, 60, 80, 100]:
    # 50
    # |- 30
    # |  |- 20
    # |  |- 40
    # |- 70
    #    |- 60
    #    |- 80
    #       |- 100
    # 70 has two children (60 and 80). Removing 70 is a two-child case.
    # Let's remove 60, which is a leaf.
    remove_value_leaf_2 = 60
    print(f"\n\nRemove {remove_value_leaf_2} (leaf):")
    bst.remove(remove_value_leaf_2)
    print(f"Tree after removing {remove_value_leaf_2}:")
    bst.print_tree(bst.root)

    # Let's remove 30, which has two children (20 and 40). Successor is 40.
    remove_value_two_children_example = 30
    print(f"\n\nRemove {remove_value_two_children_example} (two children):")
    bst.remove(remove_value_two_children_example)
    print(f"Tree after removing {remove_value_two_children_example}:")
    bst.print_tree(bst.root)


    # Now remove the root (50). Successor is minimum in right subtree (70 -> 80 -> 100), which is 80.
    remove_value_root = 50
    print(f"\n\nRemove {remove_value_root} (root with two children):")
    bst.remove(remove_value_root)
    print(f"Tree after removing {remove_value_root}:")
    bst.print_tree(bst.root)


    # --- Running Unit Tests ---
    print("\n\n--- Running Unit Tests ---")
    # Note: argv and exit=False are used so that unittest.main() doesn't
    # try to parse command-line arguments or exit the script immediately.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

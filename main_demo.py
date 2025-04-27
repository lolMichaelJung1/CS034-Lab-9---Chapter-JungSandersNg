
# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 3957

import unittest
import sys
from io import StringIO # Used for capturing print output in tests
from TreeNode import Node
from BinaryTree import BinaryTree
from BST import BST


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



# --- Command Line Interface ---
# Demonstrate the structure of a sample Binary Tree
# Demonstrate the structure of a sample BST
# Demonstrate the structure of a sample AVL Tree with balance factor (BF)

if __name__ == "__main__":
    # Control whether to run demos or unit tests
    run_tests = False  # <-- Set to True if you want to run unit tests
    if not run_tests:
        print("--- Running Example Usage ---")

        # Demo of BinaryTree (travesal methods, print_tree())
        #----------------------------------------------------
        print("\n\n------ Demo of BinaryTree (traversal methods, print_tree) ------")
        bt = BinaryTree()
        bt.root = Node('A')
        bt.root.left = Node('B')
        bt.root.right = Node('C')
        bt.root.left.left = Node('D')
        bt.root.left.right = Node('E')
        bt.root.right.right = Node('F')
        print("\nPrint the Sample Binary Tree:")
        bt.print_tree(bt.root)

        print("\nIn-order Traversal:")
        bt.inorder(bt.root)

        print("\n\nPre-order Traversal:")
        bt.preorder(bt.root)

        print("\n\nPost-order Traversal:")
        bt.postorder(bt.root)

        print("\n\n------ End of BinaryTree Demo ------")
        print("---------------------------------------------------")
        # ------------The End of Demo of BinaryTree---------------


 
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


        # Demo of AVL: insert() with balance factor
        #--------------------------------------------
        #      50
        #    /   \
        #   30    70
        #  /  \   /  \
        # 20  40 60  80
        print("\n\n------- Demo of AVLTree: insert() with balancing (show balance factors) ------")
        avl = AVLTree()
        for value in [50, 30, 70, 20, 40, 60, 80]:
            print(f"\nInserting {value} into AVL Tree:")
            avl.insert(value)
            avl.print_tree(avl.root)
            print()

        print("\n\n------ End of AVLTree Demo ------")
        print("---------------------------------------------------")

    else:
        print("--- Running Unit Tests ---\n")
        unittest.main(argv=['first-arg-is-ignored'], exit=False)

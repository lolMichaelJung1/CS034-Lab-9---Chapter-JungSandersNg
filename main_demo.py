
# Group Members: Michael Jung (ID:10680322), Timothy Sanders (), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 3957


import unittest
import sys
from io import StringIO # Used for capturing print output in tests
from TreeNode import Node
from BinaryTree import BinaryTree
from BST import BST


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

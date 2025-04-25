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



# ---Command Line Interface----
# Demo of BST: insert(), search(), remove(), inorder()
 #
 #     50
 #    /   \
 #   30    70
 #  /  \   /  \
 # 20  40 60  80
 #
  ##############################

if __name__ == "__main__":
    print("--- Running Example Usage ---")

    bst = BST()

    values = [50, 30, 70, 20, 40, 60, 80]
    for value in values:
        print(f"Inserting value: {value}")
        bst.insert(value)

    print("\n\nPrint Binary Search Tree")
    bst.print_tree(bst.root)

    print("\n\nPre-order Traversal through the BST:")
    bst.preorder(bst.root)
    print() # Add a newline after traversal output

    print("\n\nIn-order Traversal through the BST:")
    bst.inorder(bst.root)
    print()

    print("\n\nPost-order Traversal through the BST:")
    bst.postorder(bst.root)
    print()

    print("\n\nSearch for 40:")
    found_node = bst.search(40)
    if found_node:
        print(f"Found node with value: 40")
    else:
        print(f"Value 40 not found.")

    print("\n\nSearch for 100:")
    found_node = bst.search(100)
    if found_node:
        print(f"Found node with value: 100")
    else:
        print(f"Value 100 not found.")

    print("\n\nSearch for 60:")
    found_node = bst.search(60)
    if found_node:
        print(f"Found node with value: 60")
    else:
        print(f"Value 60 not found.")

    # Remove leaf node 20 (with no child)
    print("\n\nRemove 20:")
    bst.remove(20)
    bst.print_tree(bst.root)
    bst.inorder(bst.root)

    # Remove node 30 (only with right child Node(40))
    print("\n\nRemove 30:")
    bst.remove(30)
    bst.print_tree(bst.root)
    bst.inorder(bst.root)

    # Remove node 50 (with two children)
    print("\n\nRemove 50:")
    bst.remove(50)
    bst.print_tree(bst.root)
    bst.inorder(bst.root)

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
# The tree above is balanced since all the balance factors are between {-1, 0, 1}
# The Balance Factor for each node are: 50:0, 30:0,70:0, 20:0, 40:0, 60:0, 80:0
# Print AVL Tree with indentation
# Print the nodes pre-order, in-order, post-order to visualize the balancing of tree after the deletion and insertion of nodes
# ######################################################

from Node import Node
# --- AVL Tree Class ---
class AVLTree():
    def __init__(self, root=None):
        """
        Initializes an AVL Tree.

        Args:
            root: The root node of the BST. Defaults to None (empty BST).
        """
        self.root = root

    #Inorder, preorder, and postorder traversal functions
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

    def preorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node:
            print(node.key, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=' ')

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
        if Node is None and level == 0:
            node = self.root
        if node: # <-- This is the crucial base case check
            # Print the current node with indentation
            print(' ' * (5 * level) + prefix + str(node.key))
            # Only print child branches if the current node has children
            if node.left or node.right:
                 # Recursively print the left child (if it exists)
                 # Using 'L----' prefix and incrementing level
                 self.print_tree(node.left, level + 1, 'L----')
                 # Recursively print the right child (if it exists)
                 # Using 'R----' prefix and incrementing level
                 self.print_tree(node.right, level + 1, 'R----')

    """
    Balances a tree that is heavy towards the left by rotating the nodes to the right

    Args:
        left_heavy: A node that is left heavy, where the balance factor is greater than 1
    """
    def _right_rotation(self, left_heavy):
        temp = left_heavy.left
        right_sub_tree = temp.right
        left_heavy.set_child("left",right_sub_tree)
        temp.set_child("right", left_heavy)
        left_heavy.update_height()
        temp.update_height()
        return temp
    """
    Balances a tree that is heavy towards the right by rotating the nodes to the left

    Args:
        right_heavy: A node that is right heavy, where the balance factor is less than -1
    """
    def _left_rotation(self, right_heavy):
        temp = right_heavy.right
        left_sub_tree = temp.left
        right_heavy.set_child("right", left_sub_tree)
        temp.set_child("left", right_heavy)
        right_heavy.update_height()
        temp.update_height()
        return temp

    # Insert a value into the BST (recursive implementation)
    def insert(self, value):
        """
        Inserts a new value into the AVL Search Tree using recursion and balances the tree accordingly

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
            if value < node.key:
                # If the value is smaller, go to the left subtree.
                # The recursive call returns the root of the modified left subtree,
                # which we then assign back to node.left.
                # print(f"DEBUG: Going left from {node.value}") # Debug statement
                node.set_child("left", _insert(node.left, value))
            elif value > node.key:
                # If the value is larger, go to the right subtree.
                # The recursive call returns the root of the modified right subtree,
                # which we then assign back to node.right.
                # print(f"DEBUG: Going right from {node.value}") # Debug statement
                node.set_child("right", _insert(node.right, value))
            else:
                # If the value is equal, it's a duplicate. Do nothing and print a message.
                # Return the current node as the subtree remains unchanged.
                print(f"Duplicated key {value} ignored.")
                return node # Explicitly return the node

            # Return the current node. This is crucial in the recursive approach
            # as it re-links the parent node's pointer to this (potentially modified)
            # node or the new node created in the base case.

            #The height of the node is calculated to be the max height of the subtrees + 1
            node.update_height()
            #The balance factor of a node is calculated to be the height of the left subtree - height of the right subtree
            balanceFactor = node.get_balance()

            #Case 1: Left rotation
            if balanceFactor > 1 and value < node.left.key:
                return self._right_rotation(node)
            #Case 2: Right rotation
            if balanceFactor < -1 and value > node.right.key:
                return self._left_rotation(node)
            #Case 3: Left Right rotation
            if balanceFactor > 1 and value > node.left.key:
                node.set_child("left", self._left_rotation(node.left))
                return self._right_rotation(node)
            #Case 4: Right Left rotation
            if balanceFactor < -1 and value < node.right.key:
                node.set_child("right", self._right_rotation(node.right))
                return self._left_rotation(node)

            return node
        self.root = _insert(self.root, value)

    # Remove a value from the AVL Tree (recursive implementation)
    def remove(self, value):
        """
        Removes a value from the AVL Search Tree using recursion.

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
            while current and current.left:  # Added check for 'current' being not None
                current = current.left
            # Return the node found (which might be None if the input node was None)
            return current

        # Define the recursive helper function _remove
        # It takes the current node and the value to remove, updates the height of the node, verifies that the balance factor
        #is between {-1, 0, 1}, and applies rotations to balance the tree.
        #In the end the function returns the root of the (potentially modified) subtree.
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
            if value < node.key:
                # If the value is smaller, the node to remove is in the left subtree.
                # Recursively call _remove on the left child and assign the result
                # back to node.left. This re-links the parent.
                # print(f"DEBUG: Going left from {node.value}") # Debug statement
                node.left = _remove(node.left, value)
            elif value > node.key:
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
                node.key = min_node.key # Note: Uses node.key as the AVLTree class uses the Node class from TreeNode.py

                # Now, recursively remove the inorder successor from the right subtree.
                # The successor is guaranteed to have at most one right child, so
                # the recursive call will eventually hit Case 1 or Case 2.
                # Assign the result back to node.right to update the right subtree.
                # print(f"DEBUG: Recursively removing successor {min_node.value} from right subtree.") # Debug statement
                node.right = _remove(node.right, min_node.key)

            #update the height of the node
            node.update_height()

            #calculate the balance factor of the node
            balanceFactor = node.get_balance()

            #left heavy tree requires right rotation
            if balanceFactor > 1 and node.left.get_balance() >= 0:
                return self._right_rotation(node)
            #left heavy tree with a right heavy child requires left-right rotation
            if balanceFactor > 1 and node.left.get_balance() < 0:
                node.left = self._left_rotation(node.left)
                return self._right_rotation(node)
            #right heavy tree requires left rotation
            if balanceFactor < -1 and node.right.get_balance() <= 0:
                return self._left_rotation(node)
            #right heavy tree with left heavy child requires right-left rotation
            if balanceFactor < -1 and node.right.get_balance() > 0:
                node.right = self._right_rotation(node.right)
                return self._left_rotation(node)

        # Start the recursive removal process from the root.
        # The result of the recursive call (the potentially new root of the entire tree)
        # is assigned back to self.root. This handles the case where the root node
        # itself is removed.
        self.root = _remove(self.root, value)

# ---Command Line Interface----
# Demo of AVLTree: insert(), search(), remove(), inorder()
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
    print("--- AVL Tree where nodes are added in balanced order ---")
    avl_tree = AVLTree()
    avl_tree.root = Node(50)
    avl_tree.print_tree(avl_tree.root)

    avl_tree.root.left = Node(30)
    avl_tree.print_tree(avl_tree.root)

    avl_tree.root.right = Node(70)
    avl_tree.print_tree(avl_tree.root)

    avl_tree.root.left.left = Node(20)
    avl_tree.print_tree(avl_tree.root)

    avl_tree.root.left.right = Node(40)
    avl_tree.print_tree(avl_tree.root)

    avl_tree.root.right.left = Node(60)
    avl_tree.print_tree(avl_tree.root)

    avl_tree.root.right.right = Node(80)
    avl_tree.print_tree(avl_tree.root)
    print()

    print("--- AVL Tree where nodes are added in unbalanced order which is fixed using right left rotation---")
    unbalanced_tree = AVLTree()

    unbalanced_tree.insert(7)
    unbalanced_tree.print_tree(unbalanced_tree.root)

    unbalanced_tree.insert(21)
    unbalanced_tree.print_tree(unbalanced_tree.root)

    unbalanced_tree.insert(1)
    unbalanced_tree.print_tree(unbalanced_tree.root)
    print()

    print("--- AVL Tree where nodes are added in unbalanced order which is fixed using left right rotation---")
    another_unbalanced_tree = AVLTree()

    another_unbalanced_tree.insert(7)
    another_unbalanced_tree.print_tree(another_unbalanced_tree.root)

    another_unbalanced_tree.insert(6)
    another_unbalanced_tree.print_tree(another_unbalanced_tree.root)

    another_unbalanced_tree.insert(21)
    another_unbalanced_tree.print_tree(another_unbalanced_tree.root)
    print()

    print("--- AVL Tree where nodes are added in unbalanced order which is fixed using left rotation---")
    third_unbalanced_tree = AVLTree()

    third_unbalanced_tree.insert(7)
    third_unbalanced_tree.print_tree(third_unbalanced_tree.root)

    third_unbalanced_tree.insert(9)
    third_unbalanced_tree.print_tree(third_unbalanced_tree.root)

    third_unbalanced_tree.insert(100)
    third_unbalanced_tree.print_tree(third_unbalanced_tree.root)
    print()

    print("--- AVL Tree where nodes are added in unbalanced order which is fixed using right rotation---")
    fourth_unbalanced_tree = AVLTree()

    fourth_unbalanced_tree.insert(100)
    fourth_unbalanced_tree.print_tree(fourth_unbalanced_tree.root)

    fourth_unbalanced_tree.insert(90)
    fourth_unbalanced_tree.print_tree(fourth_unbalanced_tree.root)

    fourth_unbalanced_tree.insert(80)
    fourth_unbalanced_tree.print_tree(fourth_unbalanced_tree.root)
    print()

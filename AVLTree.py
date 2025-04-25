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
from BST import BST
# --- AVL Tree Class ---
class AVLTree(BST):
    def __init__(self, root=None):
        """
        Initializes an AVL Tree.

        Args:
            root: The root node of the BST. Defaults to None (empty BST).
        """
        super().__init__(root) # Call the parent BST constructor

    # Insert a value into the BST (recursive implementation)
    def insert(self, value):
        """
        Inserts a new value into the AVL Search Tree using recursion and balances the tree accordingly

        Args:
            value: The value to insert.
        """

        """
        Balances a tree that is heavy towards the left by rotating the nodes to the right

        Args:
            left_heavy: A node that is left heavy, where the balance factor is greater than 1
        """
        def _right_rotation(left_heavy):
            temp = left_heavy.left
            right_sub_tree = temp.right
            left_heavy.setChild("left",right_sub_tree)
            temp.set_child("right", left_heavy)
        """
        Balances a tree that is heavy towards the right by rotating the nodes to the left

        Args:
            right_heavy: A node that is right heavy, where the balance factor is less than -1
        """
        def _left_rotation(right_heavy):
            temp = right_heavy.right
            left_sub_tree = temp.left
            right_heavy.set_child("left", left_sub_tree)
            temp.set_child("right", right_heavy)

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

            #The height of the node is calculated to be the max height of the subtrees + 1
            node.update_height()
            #The balance factor of a node is calculated to be the height of the left subtree - height of the right subtree
            balanceFactor = node.get_balance()

            #Case 1: Left rotation
            if balanceFactor > 1 and value < node.left.key:
                return _right_rotation(node)
            #Case 2: Right rotation
            if balanceFactor < -1 and value > node.right.key:
                return _left_rotation(node)
            #Case 3: Left Right rotation
            if balanceFactor > 1 and value > node.left.key:
                node.set_child("left", _left_rotation(node.left))
                return _right_rotation(node)
            #Case 4: Right Left rotation
            if balanceFactor < -1 and value < node.right.key:
                node.set_child("right", _right_rotation(node.right))
                return _left_rotation(node)
            
            return node

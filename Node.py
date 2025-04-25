
#--------------------------------------------------------------------------------------------
# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575
#--------------------------------------------------------------------------------------------





from __future__ import annotations
from typing import Optional


class Node:
    """
    Tree node with parent node reference, along with left and right child

    Attributes
    ----------
    key
    parent : Optional[Node]
    left : Optional[Node]
    right : Optional[Node]

    Methods
    -------
    get_balance()
        Calculate the current nodes' balance factor, defined as height(left subtree) - height(right subtree)
    update_height()
        Recalculate the current height of the subtree rooted at the node, usually called after a subtree has been modified.
    set_child(which_child: str, child: Optional[Node])
        Assign either the left or right attribute with a new child.
    replace_child(current_child: Node, new_child: Node)
        Replace a current child with a new child.
    """
    parent: Optional[Node]
    left: Optional[Node]
    right: Optional[Node]

    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return f"Node (key={self.key})"

    def get_balance(self) -> int:
        """
        Calculate the current nodes' balance factor, defined as height(left subtree) - height(right subtree)

        Returns
        -------
        int
        """
        # Get the current height of left subtree, or -1 if None
        left_height = -1
        if self.left is not None:
            left_height = self.left.height
        # Get current height of right subtree, or -1 if None
        right_height = -1
        if self.right is not None:
            right_height = self.right.height

        return left_height - right_height

    def update_height(self) -> None:
        """
        Recalculate the current height of the subtree rooted at the node,
        usually called after a subtree has been modified.

        Returns
        -------
        None
        """
        # Get current height of left subtree, or -1 if None
        left_height = -1
        if self.left is not None:
            left_height = self.left.height
        # Get current height of right subtree, or -1 if None
        right_height = -1
        if self.right is not None:
            right_height = self.right.height
        # Assign self.height with calculated node height
        self.height = max(left_height, right_height) + 1

    def set_child(self, which_child: str, child: Optional[Node]) -> bool:
        """
        Assign either the left or right attribute with a new child.

        Parameters
        ----------
        which_child : str
            Which child of the node to update, "left" or "right"
        child : Optional[Node]
            The child node to be assigned to the specified location.

        Returns
        -------
        bool

        Raises
        ------
        ValueError
            If the value supplied for which_child is not "left" or "right"
        """
        if which_child not in ("left", "right"):
            raise ValueError(f"which_child must be 'left' or 'right', got {which_child!r}")
        # Assign left or right attribute
        if which_child == "left":
            self.left = child
        else:
            self.right = child

        # Assign the parent attribute of the new child, if the child has been given
        if child is not None:
            child.parent = self

        # Update the node's height, as the subtree structure may have changed
        self.update_height()
        return True

    def replace_child(self, current_child: Node, new_child: Node) -> bool:
        """
        Replace a current child with a new child.

        Parameters
        ----------
        current_child : Node
        new_child : Node

        Returns
        -------
        bool
        """
        if self.left is current_child:
            current_child.parent = None
            return self.set_child("left", new_child)
        elif self.right is current_child:
            current_child.parent = None
            return self.set_child("right", new_child)
        # If neither of the above cases apply, then the new child cannot be attached to this node.
        return False

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

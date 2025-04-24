# CS034-Lab-9---Chapter-JungSandersNg

## Binary Tree

Task:

Write a Python program that defines a binary tree using a Node class and constructs the
following tree:

sample binary tree

          A
       /    \
     B        C
    /  \       \
    D   E       F
    

Create the tree structure in code using Node objects.
Implement the following recursive traversals:

-Preorder
-Inorder
-Postorder
-Print the result of each traversal on the sample tree.

## Binary Search Tree

Task:

Implement a Binary Search Tree (BST) with the following operations:
-insert(value)
-search(value)
-remove(value)
-inorder() traversal to verify structure

## AVL Insertion

-Implement AVL Tree insertion for the same list: 50, 30, 70, 20, 40, 60, 80
-Ensure the tree self-balances by applying rotations


### Implementation Organization

1. Node Class: The Node class is fundamental to generic Binary Trees, BST, and AVL trees

2. Create a BinaryTree parent class: implement traversal methods

3. Create a BST child class that inherits from parent class BinaryTree

4. Create a AVL child class that inherits from BST class




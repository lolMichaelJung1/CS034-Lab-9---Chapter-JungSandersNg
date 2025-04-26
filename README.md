# CS034-Lab-9---Chapter-JungSandersNg

## Design And Structure

- Node class

- BinaryTree class (parent class)

- BST class (child class of BinaryTree)

- Extended AVLTree class as a child of BST (not BinaryTree)

- Proper insert() override for AVL-specific balancing and rotation



## Part 1: Binary Tree Construction and Traversal
#### Task:
Write a Python program that defines a binary tree using a Node class and constructs the
following tree:
```text
          A
       /    \
     B        C
    /  \       \
    D   E       F
```
#### Steps
1. Create the tree structure in code using Node objects.
2. Implement the following recursive traversals:
    - Preorder
    - Inorder
    - Postorder
3. Print the result of each traversal on the sample tree.
#### Requirements
- Use recursion for traversals
- Clearly label the output of each traversal
### Sample code
To view the outputs for part one, run the following code.
```shell
python BinaryTree.py
```
The output printed to the terminal should look similar to what is shown below
```text
In-order Traversal:
D B E A C F 
Pre-order Traversal:
A B D E C F 
Post-order Traversal:
D E B F C A 

Print Tree:
Root:A
     L----B
          L----D
          R----E
     R----C
          R----F
```

## Part 2: Binary Search Tree (BST) Operations
#### Task
Implement a **Binary Search Tree (BST)** with the following operations:
- `insert(value)`
- `search(value)`
- `remove(value)`
- `inorder()` traversal to verify structure
#### Steps
1. Start with an empty BST
2. Insert the following values in order: `50, 30, 70, 20, 40, 60, 80`
3. Print the tree contents in **inorder** to verify sorted order
4. Search for values `40`, `100`, and `60` - indicate whether each was found
5. Remove nodes: one with no child (`20`), one with one child (`30`), and one with two children (`50`). Print the inorder traversal after each removal.

## AVL Insertion
- Implement AVL Tree insertion for the same list: 50, 30, 70, 20, 40, 60, 80
- Ensure the tree self-balances by applying rotations


### Implementation Organization
1. Node Class: The Node class is fundamental to generic Binary Trees, BST, and AVL trees
2. Create a BinaryTree parent class: implement traversal methods
3. Create a BST child class that inherits from parent class BinaryTree
4. Create a AVL child class that inherits from BST class

class Node:
  ''' Tree node with left and right child'''
  def __init__(self, key):
      self.key = key
      self.right = None
      self.right = None

  def __str__(self):
      return f"Node (key={self.key})"

# -----------------------
# Command Line Interface
# -----------------------

'''
     A
    / \
   B   C
  / \   \
 D   E   F
'''
if __name__ == "__main__":
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')
    root.right.right = Node('F')

    print("DEBUG: Successfully Insert Nodes!")
    print(root)
    print(root.left)
    print(root.right)
    print(root.left.left)
    print(root.left.right)
    print(root.right.right)

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
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)

    print("DEBUG: Successfully Insert Nodes!")
    print(root)
    print(root.left)
    print(root.right)
    print(root.left.left)
    print(root.left.right)

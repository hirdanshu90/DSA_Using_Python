class Node:
  def __init__(self,value):
    self.left = None
    self.data = value
    self.right = None


class Tree:
  # Passing the data (value) in the node
  def createNode(self,data):
  # This function will create a new node and return it along with the data.
      return Node(data)

  

# Creating a function to insert values into the tree. 
  def insert(self, node, data):

  # If initial node is None, we will create a new node.
    if node is None:
      return self.createNode(data)

    if data < node.data:
      # Now value is inserted in the left node of the root node, so we assign the value.
      node.left = self.insert(node.left,data)

    else:
      node.right = self.insert(node.right,data)
    
    # Return first node. 
    return node
  

# Now printing the values, using in-order traversal.   (gives the values in a sorted order)
# Order: left, root, right.
# Writing a recursive function.
  
  def traverse_Inorder (self,root):
    if root is not None:
      self.traverse_Inorder(root.left)
      print(root.data)
      self.traverse_Inorder(root.right)




# Now inserting data in the tree
#  [5,2,10,7,15,12,20,30,6,8]

# Creating an object for tree
tree = Tree()
root = tree.createNode(5)
print(root.data)


# Now inserting data in the tree
tree.insert(root,2)
tree.insert(root,10)
tree.insert(root,7)
tree.insert(root,15)
tree.insert(root,12)
tree.insert(root,20)
tree.insert(root,30) 
tree.insert(root,6)
tree.insert(root,8)

print("Inorder -->")
tree.traverse_Inorder(root)
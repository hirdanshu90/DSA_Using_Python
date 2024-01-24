""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_binary_search_tree_(root):   
        
# Doing InOrder traversal, which gives the output in a sorted manner, if the list where the values will be appended, 
# is in the sorted manner, then its a BST else not. 

# Function for In_Order traversal
    def In_order(root, values):

        if root is None:
            return 
        
        In_order(root.left, values)
        values.append(root.data)
        In_order(root.right, values)
            
    
    
    values = []
    In_order(root, values)
    for i in range(len(values)-1):
        if values[i+1] <= values[i]:
            return False
    return True
    


# Traversal
# Subtle difference between printing the data and going to the last node::::

class Node:
  def __init__(self,data):
    self.data = data
    self.nref = None
    self.pref = None

class doublyLL:
  def __init__(self):
    # starting point.
    self.head = None

# Forward traversing
def forward_traversing(self):
  if self.head is None:
    print("List is empty")
  else:  
    n = self.head
    # Here cheching n is none not nref because first we want the data of the last node then exit from the code.
    while n is not None:
      print(n.data, "-->", end=" ")
      n = n.ref

# Backward traversing
# Go to last node first
# Then get the previous node
def backward_traversing(self):
    if self.head is None:
      print("List is empty")
    else:  
      n = self.head
      # n.nref because the next it should be pointing towards should be None
      while n.nref is not None:
        n = n.ref

      while n is not None:
        print(n.data, "-->", end=" ")
        n = n.pref

      

      
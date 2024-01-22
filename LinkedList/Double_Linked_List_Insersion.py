# Insertion

class Node:
  def __init__(self,data):
    self.data = data
    self.nref = None
    self.pref = None

class doublyLL:
  def __init__(self):
    # starting point.
    self.head = None

# When list is empty.
def insert_empty_node(self,data):
  if self.head is None:
    new_node = Node(data)
    self.head = new_node
  
  else:
    print("LL is not empty")

# Adding at the beginning of LL
def insert_at_beginning_node(self,data):
  if self.head is None:
    new_node = Node(data)
    self.head = new_node
  else:
    new_node = Node(data)
    new_node.nref = self.head
    self.head.pref = new_node
    self.head = new_node

# Insert the node at the end of LL
def insert_at_end_node(self,data):
  new_node = Node(data)
  if self.head is None:
    self.head = new_node

  else:
    n = self.head
    while n.nref is not None:
      n = n.nref

    n.nref = new_node
    new_node.pref = n



# Add before and after nodes.
# x is the data of the node, lets say 10, 20, 30. We have ti insert after 20, so x =20
# Check if empty.

def add_after_node(self,data,x):
  if self.head is None:
    print("Empty List")
  else:
    n = self.head
    while n is not None:
      if x == n.data:
        break
      n = n.nref

    if n is None:
      print("DAta not found")
    else:
      # Also check if we are inserting where last node or in between?
      new_node = Node(data)

      new_node.nref = n.nref
      new_node.pref = n
      n.nref = new_node

      # Checking if this is the last node or not, if not then connecting else nothing.
      if n.nref is not None:
        n.nref.pref = new_node

# ADDING NODE BEFORE.
def add_node_before_node(self, data,x):
    if self.head is None:
      print("Empty List")
    else:
      n = self.head
      while n is not None:
        if x == n.data:
          break
        n = n.nref

      if n is None:
        print("Data not found")
      else:
        new_node = Node(data)

        # Now here to check whether we are inserting before the first node.
      new_node.nref = n
      new_node.pref = n.prev


      # Checking if this is the first node or not, if not then connecting else nothing.
      if n.nref is not None:
        n.pref.nref = new_node
      else:
        # If yes, updating the head.
        self.head = new_node
      n.prev = new_node
      


  
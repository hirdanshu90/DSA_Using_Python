# Creating a Node
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
# This class defines a simple node for a linked list. 
# Each node has two attributes: data to store the value of the node, and ref (reference) to point to the next node in the linked list.
        

# Creating a Linked List

class LinkedList():
    def __init__(self):
        self.head = None  
        # This is the head of the linked list
# This class initializes an empty linked list with a head attribute set to None. The head is the starting point of the linked list.

#  traversing through linked lists.
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref


# Insertion elements (At the beginning of the list)
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        # Creating a new node, then referencing it to the 1st node that is the head node,
        # then changing the head node to this newly created node.


    # Inserting a new node (at the end of the node)

    def add_last(self,data):
        new_node = Node(data)
        

    # Checking if the LL is empty or not?
        if self.head is None:
            self.head = new_node
        else:
            # Taking a pointer here to reach the end of the LL.
            pointer = self.head
            while pointer.ref is not None:
                pointer = pointer.ref
            # Now we are at the last node. assigning the pointer to the new node
            pointer.ref = new_node


# Add node after a particular node

    # x is the node after which we should add.
    # METHOD: find x node, compare data of self.head to x, traverse,
    def after_node(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
              break
            n = n.ref
      # Here either we found x or None is returned
        if n is None:
            print("No node found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


# How to add an element before a given node.
      # x is the data element before which we have to insert, 


      # First case, adding before the first element.
    def add_before(self,data,x):
        if self.head is None:
            print("Linked list is empty, nothing")
            return 
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        
    # Case2: adding before the previous node. 
    #  First finding the PREVIOUS node then just adding.

        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("No Node found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        

# Inserting when Linked List is empty:

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("No Linked List is empty")

        
# DELETE OPERATIONS FROM LL.

    # Check if LL is empty or not
    def delete_begin(self):
        if self.head is None:
            print("No Node found")
        else:
            self.head = self.head.ref 


# DELETE last node of LL

    def delete_end(self):
        if self.head is None:
            print("No Node found")
        # Condition if only one node is there
        elif self.head.ref is None:
            self.head = None

        else:
            # Find second last node.
            n = self.head
            while n.ref.ref is not None:
                n = n.ref

        n.ref = None


# Delete any node for the middle:

    def delete_any(self, x):
        if self.head is None:
            print("No Node found")
            return
        
        # Checking if its the first node 
        if x == self.head.data:
            self.head = self.head.ref
            return
        
     # Now finding the node before x ( We check n.ref for none not n )
        n = self.head
        while n.ref is not None:
            if x ==  n.ref.data:
                break
            n = n.ref

        if n.ref is None:
            print("No Node found")
        else:
            n.ref = n.ref.ref






LL1 = LinkedList()
LL1.add_begin(1)
LL1.add_last(1000)
LL1.add_begin(23)
LL1.add_begin(75)

LL1.after_node(69,1)
LL1.delete_begin()
LL1.delete_end()
LL1.print_LL()






    
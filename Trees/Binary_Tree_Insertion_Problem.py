class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

# We have to Complete the Insert Function in the problem in an  ITERATIVE manner
    def insert(self, val):

        # Checking if there is a root node or not.
        if self.root is None:
            self.root = Node(val)
            return
            
        # Assigning Self.root in the temp variable, to keep its value
        root = self.root
        
        # Working with the infinite loop because no idea how many nodes are there, and until the break statement hits.
        while 1:

        # Left Side
            if val < root.info:
                if root.left is not None:
                    # Going till the last Left node 
                    root = root.left
                else:
                    # When hit none, then create a new node for new inserting value
                    root.left = Node(val)
                    break
                
        # Right Side
            else:
                if root.right is not None:
                    root = root.right
                else:
                    root.right = Node(val)
                    break
                    
        return self.root
                
        
# ignore the last part, FOCUS on the insertion function, and how node is defined.
        
tree = BinarySearchTree()

arr = [9, 3 ,5 ,1 ,8 ,12, 11,16, 2 ,4 ,6]

# individually all the elements of the array goes through the code and tree is made ...... 
for i in range(len(arr)):
    tree.insert(arr[i])

preOrder(tree.root) 
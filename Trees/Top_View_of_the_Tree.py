

# Each node has 4 attributes here: 

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 


def topView(root):
    
    # queue, FIFO property used here.....
    q = []
    d = dict()
    
    # We have 4 parts in the tree: [ left, info, level, right ]
    # For level, we will, start from 0, and for left, we do -1 and for right +1 (Both calculations are with the respect to ROOT value level i.e. 0 taken here ). This will ensure the uniqueness.
    # And dict will maintain the unique value as we will do InOrder Traversal, and the values that will have the same keys (they will be in the shadow i.e. not visible from the top view and will not be printed in the final result)
    
    root.level = 0
    q.append(root)
    
    while len(q) != 0:
        
        root = q.pop(0)
        
        if root.level not in d: 
            # level value will be the key. 
            d[root.level] = root.info 
            
        if root.left is not None:
            q.append(root.left)
            root.left.level = root.level - 1
            
        if root.right is not None:
            q.append(root.right)
            root.right.level = root.level + 1
            
    # Printing the dict values in a single line format ......
    for i in sorted(d):
        print(d[i], end=' ')
     
    
        
    
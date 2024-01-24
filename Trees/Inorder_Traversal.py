# We need to print the nodes level by level. We process each level from left to right. 

def levelOrder(root):

    # Queue
    q = []
    
    # Adding the root node
    q.append(root)
    
    # Loop will work till queue is empty
    while len(q) != 0:
        
        # We remove the first element (root)
        root = q.pop(0)
        
        # Printing in a single line, so used end=' '
        print(root.info, end=' ')
        
        # Checking for further nodes left and right, if present, then appending them to the queue
        if root.left is not None:
            q.append(root.left)
            
        if root.right is not None:
            q.append(root.right)
    
   
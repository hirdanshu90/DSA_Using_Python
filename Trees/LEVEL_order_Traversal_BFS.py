# We need to print the nodes level by level. We process each level from left to right. 
# Level Order Traversal technique is defined as a method to traverse a Tree such that all nodes present in the same level are traversed completely before traversing the next level.

# Level Order Traversal (Breadth First Search or BFS) of Binary Tree

def levelOrder(root):

    # Queue, FIFO property used here......
    q = []
    
    # Adding the root node itself not the value of the queue.
    q.append(root)
    
    # Loop will work till queue is empty
    while len(q) != 0:
        
        # We remove the first element (root)
        root = q.pop(0)
        
        # Printing in a single line, so used end=' '. AND we append the value and not the ROOT node.
        print(root.val, end=' ')
        
        # Checking for further nodes left and right, if present, then appending them to the queue

        # We can append in any order based on our QUESTION need... Right or left node.
        if root.left is not None:
            q.append(root.left)
            
        if root.right is not None:
            q.append(root.right)

# This will print the values in a single line. 


# Time Complexity: O(N) where N is the number of nodes in the binary tree.
# Auxiliary Space: O(N) where N is the number of nodes in the binary tree.



                    #  ........... OR ...................


# But if we want to print the values like level by level in separate arrays then: 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        q = [root]  # Initialize the queue with the root node
        arr = []

        while q:
            current_arr = []

            # Process all nodes at the current level
            for _ in range(len(q)):
                node = q.pop(0)  # Dequeue the front node
                current_arr.append(node.val)  # Append the value of the current node

                # Enqueue the left and right children of the current node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            arr.append(current_arr)  # Append the values of the current level to the result

        return arr
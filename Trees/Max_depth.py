# Max depth/height measures the maximum downward distance from the root to a leaf.
# (Basically max number of nodes along the way so we add 1, when doing recurrsively.)

# .......... Can be solved using 3 approaches........


# APPROACH 1 : Recursive DFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    
            # Base Case
            if root is None: 
                return 0
    
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# APPROACH 2 : BFS Iteratively: ( Level Order Solution )
        
# Here we calculate the number of levels == Depth of the Tree. 
# We solve BFS by using Queue data structure.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
            
        if not root:
            return 0
        q = []
        q.append(root)
        level = 0

        while len(q) != 0:
# Here since we are not printing all the nodes or counting, we run a FOR loop inside to remove all the nodes at a certain level all at once,
# so that it is counted as 1 level and not separately.
            for i in range(len(q)):
                root = q.pop(0)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
                        
            level += 1
                
        return level


# APPROACH 3 : DFS Iteratively: 
    
# Doing PREorder DFS using stack data structure.
    
class Solution:
    def maxDepth(root) -> int:
            
        if not root:
            return 0
                
        # Maintaining Node and depth in the stack
        stack = [[root,1]]  # Initialize a stack with the root node and its depth
        res = 1             # Initialize the maximum depth as 1

        while stack:


            # WHENEVER we will encounter a NULL node, we will pop the element off the stack, else, we will add to the stack SIMPLE.
            node, depth = stack.pop(0)  # Pop the node and its depth from the stack

            # This if statement will prevent from using None node, if they are present in the Stack .. ....
            if node is not None:
                res = max(res,depth)    # Update the maximum depth if necessary
                stack.append([node.left, depth+1])   # Add the left child and its depth to the stack
                stack.append([node.right, depth+1])  # Add the right child and its depth to the stack

        return res
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# The length of a path between two nodes is represented by the number of edges between them.

#  We calculate the height of each node. H = 1 + max(left,right) 

#  Then diameter is =  Height_left + Height_right.   

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Taking a global variable as an array 1st element. 
        # Using a list with a single element allows the code to maintain a mutable reference to the diameter value, enabling updates to it within the recursive function.
        res = [0]

        def dfs(root):  

            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            # Update the diameter if the sum of left and right subtree heights is greater
            res[0] = max(res[0], left + right)

            # Return the height of the current node's subtree
            return 1 + max(left, right)

        # Start depth-first search (DFS) from the root
        dfs(root)
        
        # Return the calculated diameter
        return res[0]
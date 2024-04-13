

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Question is from any node to any node.........

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Initialize a list to store the result
        res = [root.val]  # We use a list to store the result to be able to modify it within the DFS function
        
        # Define a Depth-First Search (DFS) function to traverse the tree
        def dfs(root):
            # Base case: if the current node is None, return 0
            if root is None:
                return 0

            # Recursively calculate the maximum sum path in the left subtree
            leftMax = dfs(root.left)
            # Recursively calculate the maximum sum path in the right subtree
            rightMax = dfs(root.right)

            # If the maximum sum path in the left subtree is negative, consider it as 0
            leftMax = max(leftMax, 0)
            # If the maximum sum path in the right subtree is negative, consider it as 0
            rightMax = max(rightMax, 0)

            # Update the maximum result if the sum of the current node, left subtree, and right subtree is greater
            # FOR each node we calculate the sum and store the result.
            res[0] = max(res[0], root.val + leftMax + rightMax)

            # Return the maximum sum path that can be extended from the current node
            return root.val + max(leftMax, rightMax)
        
        # Start the Depth-First Search (DFS) from the root of the tree
        dfs(root)

        # Return the maximum path sum found during the traversal
        return res[0]

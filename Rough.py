# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(root):

        if root is None:
            return 0

        # Maintaining Node and depth in the stack
        stack = [[root,1]]
        res = 1

        while stack:

            node, depth = stack.pop(0)
            # This if statement will prevent from using None node, if they are present in the Stack .. ....
            
            if node is not None:
                res = max(res,depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res

        
root = [3,9,20,15,7]
tree = Solution
print(tree.maxDepth(root))
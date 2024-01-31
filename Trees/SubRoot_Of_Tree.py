"""
To determine if subRoot is a subtree of root, you need to perform a tree traversal that checks if a subtree rooted at any node of root is identical to subRoot. This typically involves a recursive approach where you compare nodes of root and subRoot recursively.

Here's a high-level approach:

    Start a recursive function that traverses the tree rooted at root.
    At each node encountered during traversal, check if it's identical to the root of the subtree subRoot.
    If it is, perform a recursive check to verify if the subtree rooted at this node matches subRoot.
    If a match is found, return True. Otherwise, continue traversing the tree.
    If no match is found after traversing the entire tree, return False.

    ALWAYS look at the EDGE cases, if they are NULL, one of them is NULL etc
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:

        # Seeing the edge cases....
        if subroot is None:
            return True
        if root is None:
            return False
        
        if self.sameTree(subroot,root):
            return True

        # Now the trick, we can compare the subtree to left and right of the root tree as well ......
        return ( self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot) )



# Helper Function to compare the trees.
    def sameTree(self,s,t):

        # edge/base cases
        if s is None and t is None:
            return True
        
        if s is None or t is None:
            return False
        
        # Here now if root values are same, then further checking their child nodes recursively then .......
        if s is not None and t is not None and s.val == t.val:
            return ( self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right) )


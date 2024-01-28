# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

# isBalanced only returns boolean

# Basically, recursion will do its job and find the height, main task is to compare and write the logic for balanced, checking 3 conditions for True case.
# Also see the array, how results are stored, rather than using variables

        def dfs(root):
            # Base case: If the node is None, it's balanced with height 0
            if root is None:
                # Return a list indicating balance status and height [balance, height]
                return [True, 0]

            # Recursive calls to find balance and height of left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # Check if both subtrees are balanced and their heights differ by at most 1
            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                balanced = True
            else:
                balanced = False

            # Return balance status and height of the current subtree
            return [balanced, 1 + max(left[1], right[1])]

        # Call the recursive function and return the balance status
        return dfs(root)[0]

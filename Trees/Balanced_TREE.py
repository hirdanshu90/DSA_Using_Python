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

            # Check if both subtrees are balanced and their heights differ by at most 1. If there is any False, then over.
            if left[0] and right[0] and abs(left[1] - right[1]) <= 1:
                balanced = True
            else:
                balanced = False

            # Return balance status and height of the current subtree
            return [balanced, 1 + max(left[1], right[1])]

        # Call the recursive function and return the balance status
        return dfs(root)[0]


# In the Depth-First Search (DFS) function provided, the comparison of the left and right subtrees' balance status and height is done after the DFS calls for both the left and right subtrees have been made. This might give an impression that both are compared simultaneously, but in fact, they are not.

"""

Let's clarify the process:

1. **DFS on Left Subtree**:
    - The function first performs a DFS call on the left subtree (`dfs(root.left)`).
    - This call explores the left subtree completely until it reaches a leaf node or a node with a `None` child, computing the balance status and height of each subtree along the way.
    - These values (balance status and height) are stored in the variable `left`.

2. **DFS on Right Subtree**:
    - After the left subtree has been fully explored, the function proceeds to perform a DFS call on the right subtree (`dfs(root.right)`).
    - Similarly, the right subtree is explored fully, and the balance status and height of each subtree are computed and stored in the variable `right`.

3. **Comparison and Return**:
    - Once both the left and right subtrees have been explored and their balance status and height have been computed, the function compares these values to determine the balance status of the current node.
    - It checks if both the left and right subtrees are balanced and if the difference in their heights is at most 1.
    - Based on this comparison, it determines the balance status of the current node.
    - The balance status of the entire tree is determined based on the balance status of its subtrees, and it is returned by the function.

So, to clarify, the left and right subtrees are not compared simultaneously. Instead, the DFS function explores the left subtree first, then the right subtree, and finally compares their balance status and height to determine the balance status of the current node and, ultimately, of the entire tree.


"""
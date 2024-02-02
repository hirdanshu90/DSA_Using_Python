
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Construct a binary tree from preorder and inorder traversals.

        Args:
        - preorder: List of integers representing the preorder traversal of the tree.
        - inorder: List of integers representing the inorder traversal of the tree.

        Returns:
        - Optional[TreeNode]: The root of the constructed binary tree.
        """
        # However, in Python, lists are not None by default. Instead, they may be empty lists []. 
        # Therefore, the base case should be modified to check for empty lists rather than None.
        
        # Base case: Check if either preorder or inorder lists are empty
        if not preorder or not inorder:
            return None

        # Create the root node using the first element of preorder
        root = TreeNode(preorder[0])

        # Find the index of the root node's value in the inorder traversal
        mid = inorder.index(preorder[0])

        # Recursively build the left subtree using elements from preorder and inorder
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # Recursively build the right subtree using elements from preorder and inorder
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        # Return the root of the constructed binary tree
        return root


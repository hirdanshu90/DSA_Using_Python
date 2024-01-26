# Max depth/height measures the maximum downward distance from the root to a leaf.

def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None: 
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

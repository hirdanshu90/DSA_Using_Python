# Max depth/height measures the maximum downward distance from the root to a leaf. (Basically max number of nodes along the way so we add 1, when doing recurrsively.)

# Can be solved using 3 approaches........


# APPROACH 1 : Recurrsive DFS

def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Base Case
        if root is None: 
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# APPROACH 2 : Without Recurrsion: 

# BFS Iteratively: ( Level Order Solution )
        
# Here we calculate the number of levels == Depth of the Tree. 
# We solve BFS by using Queue data structure.

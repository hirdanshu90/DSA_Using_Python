# Can also be solved using DFS Recursively easily.

# Solved using DFS Iteratively......

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # Initialize variables
        n = 0  # Counter for the number of visited nodes
        stack = []  # Stack for iterative traversal
        curr = root  # Pointer to track the current node

        # Perform in-order traversal iteratively
        while curr or stack:  # Continue traversal until there are nodes to explore or the stack is not empty
            while curr:  # Traverse to the leftmost node of the current subtree
                stack.append(curr)  # Push nodes onto the stack
                curr = curr.left  # Move to the left child
            
            curr = stack.pop()  # Pop the top node from the stack (most recent left node)
            n += 1  # Increment the count of visited nodes

            if n == k:  # If the current node is the kth smallest node
                return curr.val  # Return the value of the current node

            curr = curr.right  # Move to the right child to explore its subtree

        # If the kth smallest element is not found in the BST
        return -1  # Return -1 (or handle the case according to requirements)

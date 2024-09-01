# Testing If I can write the code ........
# Actual code with explanation is in the next file .....

def levelOrder(root):
    if root is None:
        return
    # Track karne ke liye queue, q will have the nodes
    q = [root]
    # This arr is returned, this will have the valuessss
    res = []
    while q:
        # This arr is stored according to levels in res
        curr_arr = []
        for i in range(len(q)):
            node = q.pop()
            curr_arr.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(curr_arr)


# Using deque

from collections import deque

def levelOrder(root):
    if root is None:
        return []

    q = deque([root])  # Initialize the deque with the root
    result = []

    while q:
        level_size = len(q)
        current_level = []

        for _ in range(level_size):
            node = q.popleft()  # Efficiently pop from the front
            current_level.append(node.val)

            if node.left:
                q.append(node.left)  # Append children to the back
            if node.right:
                q.append(node.right)

        result.append(current_level)

    return result

    

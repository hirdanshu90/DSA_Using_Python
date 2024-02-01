

DIFFERENCES:

Binary Tree: A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left child and the right child.

Binary Search Tree (BST): A binary search tree is a specific type of binary tree in which the left child of a node contains only nodes with values less than the node's value, and the right child contains only nodes with values greater than the node's value.

- - - - - - Below are the Tree traversals through DFS using recursion - - - - - - - 

Printing values in the tree. 

In the context of tree traversal, there are three common methods to print values:

tree = [5,2,9, .....]

CAN identify based on the root location:  if first then PreOrder, if in middle then In Order, if at last then PostOrder. 

NOTE: EXAMPLE shown in the recursive manner. 

1. **In-Order Traversal:**
   - Traverse the left subtree.
   - Visit the root node.
   - Traverse the right subtree.
   -  OUTPUT is printed in the SORTED manner (Eg: if want to print Binary Search tree in sorted order)
  
  OUTPUT: (2,5,9)


   CODE: 
   
# Function for In_Order traversal, that will store the values in the array, and return that, so that we can perform actions on it.
   def In_order(root, values):

      if root is None:
         return 
      
      In_order(root.left, values)
      values.append(root.data)
      In_order(root.right, values)
         
   
   
   values = []
   In_order(root, values)
   for i in range(len(values)-1):
      if values[i+1] <= values[i]:
         return False
   return True

Time Complexity: O(N)
Auxiliary Space: O(log N)

USES: if you want to get the nodes of a BST in non-increasing order, you simply perform a reversed inorder traversal where you start from the right subtree, visit the current node, and then move to the left subtree. This way, you'll get the nodes from largest to smallest.



2. **Pre-Order Traversal:**
   - Visit the root node.
   - Traverse the left subtree.
   - Traverse the right subtree.
   
  OUTPUT: (5,2,9)

   ```python
   def print_pre_order(node):
       if node is not None:
           print(node.value)
           print_pre_order(node.left)
           print_pre_order(node.right)
   ```

USES: So, in simple terms, preorder traversal helps in creating a copy of a tree by following a specific order of visiting nodes, and it also helps in obtaining prefix expressions from expression trees by visiting the nodes in a particular order.



3. **Post-Order Traversal:**
   - Traverse the left subtree.
   - Traverse the right subtree.
   - Visit the root node.

     OUTPUT: (2,9,5)
   
   ```python
   def print_post_order(node):
       if node is not None:
           print_post_order(node.left)
           print_post_order(node.right)
           print(node.value)
   ```

USES: In simple terms, postorder traversal is useful for safely deleting a tree because it allows you to deallocate memory in a systematic manner, starting from the bottom nodes. Additionally, it helps in obtaining postfix expressions from expression trees by visiting nodes in a specific order.

These three traversal methods provide different orders in which the nodes of the tree are visited and, consequently, different sequences of values are printed. The choice of traversal method depends on the requirements of the specific problem you are solving.


........... HIGHER and LOWER levels in the tree..............


In the context of a tree structure, "higher" and "lower" levels refer to the distance of a particular node from the root of the tree.

1. **Higher Level**:
   - Nodes that are closer to the root of the tree are considered to be at higher levels.
   - The root node itself is at the highest level because it is the starting point of the tree.

2. **Lower Level**:
   - Nodes that are farther away from the root, deeper into the tree, are considered to be at lower levels.
   - As you move down the tree from the root, each subsequent level represents nodes that are further away from the root.

For example, consider a simple binary tree:

```
       A             <- Level 1 (Root)
     /   \
    B     C         <- Level 2
   / \   / \
  D   E F   G       <- Level 3
```

- In this tree, node A is at level 1 because it's the root.
- Nodes B and C are at level 2 because they are directly below the root.
- Nodes D, E, F, and G are at level 3 because they are one level below nodes B and C.

So, when we talk about visiting nodes in "lower levels before higher levels" during level order traversal, we mean that we visit nodes closer to the root first and then proceed to nodes deeper into the tree.

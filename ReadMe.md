

DIFFERENCES:

Binary Tree: A binary tree is a hierarchical data structure where each node has at most two children, referred to as the left child and the right child.

Binary Search Tree (BST): A binary search tree is a specific type of binary tree in which the left child of a node contains only nodes with values less than the node's value, and the right child contains only nodes with values greater than the node's value.

- - - - - - - - - - - Below are the Tree traversals through DFS using recursion - - - - - - - - - - 

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
   ```python
   def print_in_order(node):
       if node is not None:
           print_in_order(node.left)
           print(node.value)
           print_in_order(node.right)
   ```

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

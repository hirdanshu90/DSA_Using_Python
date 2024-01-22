Printing values in the tree. 

In the context of tree traversal, there are three common methods to print values:

tree = [5,2,9, .....]

CAN identify based on the root location:  if first then PreOrder, if in middle then In Order, if at last then PostOrder

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

These three traversal methods provide different orders in which the nodes of the tree are visited and, consequently, different sequences of values are printed. The choice of traversal method depends on the requirements of the specific problem you are solving.
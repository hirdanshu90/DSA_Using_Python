POINTS TO REMEMBER: 

- The topmost node in a binary tree is called the ROOT, and the bottom-most nodes are called LEAVES

The most important points is: 

- BFS starts visiting nodes from root WHILE DFS starts visiting nodes from leaves. 
- So if our problem is to search something that is more likely to closer to root, we would prefer BFS. And if the target node is close to a leaf, we would prefer DFS.


QUESTION : Exercise: Which traversal should be used to print leaves of Binary Tree and why? 
         : Which traversal should be used to print nodes at k’th level where k is much less than total number of levels? 

- To print leaves of a Binary Tree: Use Inorder traversal (DFS).
- To print nodes at k'th level where k is much less than total number of levels: Use Level Order traversal (BFS).


 - The maximum number of nodes at level ‘l’ of a binary tree is 2l
 - The level of the root is 0
 - The Maximum number of nodes in a binary tree of height ‘h’ is 2h – 1:  Note: Here the height of a tree is the maximum number of nodes on the root-to-leaf path. The height of a tree with a single node is considered as 1

................ TYPES of Binary Tree .................

Binary trees can be classified into various types based on their structure, properties, and usage. Here are some common types of binary trees with examples:

1. **Full Binary Tree**:
   - In a full binary tree, every node has either 0 or 2 children.
   - Example:
     ```
           1
         /   \
        2     3
       / \   / \
      4   5 6   7
     ```

A Binary Tree is a full binary tree if every node has 0 or 2 children. The following are examples of a full binary tree. We can also say a full binary tree is a binary tree in which all nodes except leaf nodes have two children.


2. **Complete Binary Tree**:
   - In a complete binary tree, all levels are completely filled except possibly for the last level, which is filled from left to right.
   - Example:
     ```
           1
         /   \
        2     3
       / \   /
      4   5 6
     ```

3. **Perfect Binary Tree**:
   - In a perfect binary tree, all internal nodes have exactly two children, and all leaf nodes are at the same level.
   - Example:
     ```
           1
         /   \
        2     3
       / \   / \
      4   5 6   7
     ```

4. **Balanced Binary Tree**:
   - In a balanced binary tree, the height of the left and right subtrees of any node differ by at most one.
   - Example:
     ```
           1
         /   \
        2     3
       / \   / \
      4   5 6   7
     ```

5. **Degenerate (or Pathological) Binary Tree**:
   - In a degenerate binary tree, each parent node has only one associated child node.
   - Example:
     ```
           1
            \
             2
              \
               3
                \
                 4
     ```

6. **Skewed Binary Tree**:
   - A skewed binary tree is a special case of a degenerate binary tree where the tree is either completely left-skewed or completely right-skewed.
   - Example of a left-skewed tree:
     ```
           1
          /
         2
        /
       3
      /
     4
     ```

These are some common types of binary trees, each with its own characteristics and applications in various algorithms and data structures.

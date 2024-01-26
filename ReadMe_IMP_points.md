POINTS TO REMEMBER: 

The most important points is, 
BFS starts visiting nodes from root while DFS starts visiting nodes from leaves. 
So if our problem is to search something that is more likely to closer to root, we would prefer BFS. And if the target node is close to a leaf, we would prefer DFS.


QUESTION: Exercise: Which traversal should be used to print leaves of Binary Tree and why? 
          Which traversal should be used to print nodes at k’th level where k is much less than total number of levels? 

To print leaves of a Binary Tree: Use Inorder traversal (DFS).
To print nodes at k'th level where k is much less than total number of levels: Use Level Order traversal (BFS).

# Breadth-First Search (BFS) for Binary Trees (also called Level-Order Traversal):
# BFS is a traversal algorithm that explores a binary tree level by level, visiting all nodes at one depth before moving on to nodes at the next depth.
# In binary trees, BFS is commonly referred to as level-order traversal.
# The algorithm uses a queue to keep track of the nodes that need to be explored.

# Steps for BFS traversal in a binary tree:
# 1. Start with the root node.
# 2. Enqueue the root node.
# 3. While the queue is not empty:
#    a. Dequeue the front node.
#    b. Process the node (e.g., print or store its value).
#    c. Enqueue the left child of the dequeued node (if it exists).
#    d. Enqueue the right child of the dequeued node (if it exists).
# 4. Repeat the process until the queue is empty (i.e., all levels of the tree are traversed).

# Key points:
# - BFS for binary trees ensures that all nodes at each level are visited before moving on to the next level.
# - It uses a queue to maintain the order in which nodes should be visited.
# - This traversal is useful for scenarios where nodes need to be processed in level order (e.g., finding the shortest path in unweighted binary trees).
#

# BFS for binary trees can be used for:
# - Printing or processing the nodes level by level (level-order traversal).
# - Finding the shortest path from the root to a target node in an unweighted binary tree.
# - Solving problems where tree nodes need to be processed in breadth-first order, such as calculating the width of the tree at each level.
#
# Important considerations:
# - BFS is not recursive and relies on a queue for its iterative approach.
# - It processes nodes in increasing order of their depth (distance from the root).

# Example of BFS (level-order traversal) in a binary tree:
class Node:
     def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None

from collections import deque

def bfs_binary_tree(root):
    if not root:
         return
     
    queue = deque([root])  # Initialize the queue with the root node

    while queue:
        node = queue.pop()  # Dequeue the front node
        print(node.value)       # Process the node (e.g., print its value)
        
        if node.left:
            queue.append(node.left)  # Enqueue the left child
        
        if node.right:
            queue.append(node.right)  # Enqueue the right child

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
bfs_binary_tree(root)

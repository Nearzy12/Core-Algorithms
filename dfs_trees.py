# Depth-First Search (DFS) for Binary Trees:
# DFS is a recursive algorithm used to traverse or search through a binary tree by visiting nodes in depth order.
# There are three main types of DFS traversals for binary trees:
# 
# 1. Preorder Traversal (Node -> Left -> Right):
#    - Visit the current node first.
#    - Recursively traverse the left subtree.
#    - Recursively traverse the right subtree.
# 
# 2. Inorder Traversal (Left -> Node -> Right):
#    - Recursively traverse the left subtree.
#    - Visit the current node.
#    - Recursively traverse the right subtree.
# 
# 3. Postorder Traversal (Left -> Right -> Node):
#    - Recursively traverse the left subtree.
#    - Recursively traverse the right subtree.
#    - Visit the current node.
# 
# DFS in binary trees uses recursion or an explicit stack to keep track of the current path.
# Common uses include tree searches, tree traversals for sorting, and evaluating mathematical expressions (postfix, prefix).
#
# Example for Preorder Traversal in Python:
# def dfs_preorder(node):
#     if node:
#         print(node.value)          # Process the current node
#         dfs_preorder(node.left)    # Traverse the left subtree
#         dfs_preorder(node.right)   # Traverse the right subtree

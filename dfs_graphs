# Depth-First Search (DFS) for Graph Traversals:
# DFS is a graph traversal algorithm that explores as far as possible along a path before backtracking.
# It works on both directed and undirected graphs and is often implemented using recursion or an explicit stack.
# DFS explores a graph by visiting nodes (or vertices) and their adjacent nodes (or neighbors) in depth order.

# Steps for DFS traversal in a graph:
# 1. Start from a given node (or vertex).
# 2. Mark the current node as visited to avoid revisiting it later.
# 3. Recursively explore each unvisited neighbor of the current node, going as deep as possible.
# 4. Backtrack when you encounter a node with no unvisited neighbors, and explore other paths.
# 
# Key points:
# - It can be implemented recursively or using an explicit stack for iterative traversal.
# - DFS is often used to explore connected components of a graph.
# - It is useful for solving problems like pathfinding, detecting cycles, and topological sorting (in directed acyclic graphs).
# - DFS may not necessarily find the shortest path between nodes, as it prioritizes depth over breadth.

# Example of DFS in an undirected or directed graph using an adjacency list:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
#
# def dfs_graph(node, visited):
#     if node not in visited:
#         visited.add(node)              # Mark the node as visited
#         print(node)                    # Process the node (e.g., print or store it)
#         for neighbor in graph[node]:   # Traverse each neighbor of the current node
#             dfs_graph(neighbor, visited)
#
# visited = set()  # To track visited nodes
# dfs_graph('A', visited)

# DFS in a graph can be used for:
# - Finding all connected components in a graph.
# - Checking for cycles in both directed and undirected graphs.
# - Topological sorting in directed acyclic graphs (DAGs).
# - Solving maze or puzzle problems represented as graphs.
# 
# Important considerations:
# - In directed graphs, pay attention to the direction of edges when traversing neighbors.
# - For unconnected graphs, you may need to run DFS from multiple starting points to explore all nodes.

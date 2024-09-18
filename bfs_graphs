# Breadth-First Search (BFS) for Graph Traversals:
# BFS is a graph traversal algorithm that explores all nodes at the present depth level before moving on to nodes at the next depth level.
# It works for both directed and undirected graphs and is typically implemented using a queue to keep track of the nodes to explore.
# BFS explores the graph layer by layer, making it ideal for finding the shortest path in an unweighted graph.
#
# Steps for BFS traversal in a graph:
# 1. Start from a given node (or vertex).
# 2. Enqueue the starting node and mark it as visited.
# 3. While the queue is not empty:
#    a. Dequeue the front node.
#    b. Process the node (e.g., print or store it).
#    c. Enqueue all unvisited neighbors of the dequeued node and mark them as visited.
# 4. Repeat this process until the queue is empty (i.e., all reachable nodes are visited).
#
# Key points:
# - BFS uses a queue to keep track of nodes that need to be explored.
# - It explores all nodes at the current depth level before moving to the next level.
# - BFS is often used to find the shortest path in an unweighted graph since it explores nodes in the order of their distance from the starting point.
# - Unlike DFS, BFS does not go deep into a branch but instead explores neighbor nodes first.
#
# Example of BFS in an undirected or directed graph using an adjacency list:
# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }
#
# from collections import deque
#
# def bfs_graph(start_node):
#     visited = set()                # To track visited nodes
#     queue = deque([start_node])    # Initialize the queue with the start node
#     visited.add(start_node)        # Mark the start node as visited
#     
#     while queue:
#         node = queue.popleft()     # Dequeue the front node
#         print(node)                # Process the node (e.g., print or store it)
#         
#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append(neighbor)  # Enqueue unvisited neighbors
#                 visited.add(neighbor)   # Mark them as visited
#
# bfs_graph('A')
#
# BFS can be used for:
# - Finding the shortest path in an unweighted graph.
# - Level-order traversal in trees (as trees are a special case of graphs).
# - Discovering all connected components in an undirected graph.
# - Solving problems like the "shortest path in a maze" where BFS explores paths based on proximity to the start point.
#
# Important considerations:
# - BFS will explore all reachable nodes from the starting node, but if the graph is disconnected, you'll need to initiate BFS from multiple starting points.
# - In a directed graph, pay attention to the direction of the edges when enqueuing neighbors.

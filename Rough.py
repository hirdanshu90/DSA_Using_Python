def dfs(graph, node, visited):
    visited = set()  # Set to keep track of visited nodes
    
    # Mark the node as visited
    visited.add(node)
    
    # Process the node (e.g., print it)
    print(node, end=" ")

    # Recursively visit all the unvisited neighbors
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
# Example graph represented as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
# Perform DFS starting from node 0
dfs(graph, 0, visited = None)
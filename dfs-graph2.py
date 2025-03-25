graph = {
    'A': ['B', 'C'],
    'B': ['A', 'E', 'D', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

def dfs(graph, node, visited=set()):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("\nDFS Traversal:")
dfs(graph, 'A')

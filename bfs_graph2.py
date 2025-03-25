from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'E', 'D', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

print("BFS Traversal:")
bfs(graph, 'A')

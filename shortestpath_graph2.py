import heapq

graph = {
    'A': {'B': 3, 'C': 1},
    'B': {'A': 3, 'E': 1, 'D': 5, 'C': 7},
    'C': {'A': 1, 'B': 7, 'D': 2},
    'D': {'B': 5, 'C': 2, 'E': 7},
    'E': {'B': 1, 'D': 7}
}

def dijkstra(graph, start, target):
    pq = [(0, start)] 
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    parent = {node: None for node in graph}

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node == target:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                parent[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    path = []
    node = target
    while node:
        path.append(node)
        node = parent[node]
    
    return distances[target], list(reversed(path))

shortest_distance, shortest_path = dijkstra(graph, 'A', 'E')
print(f"Shortest Path: {shortest_path}, Distance: {shortest_distance}")

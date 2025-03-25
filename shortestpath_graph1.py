import heapq

graph = {
    'A': {'B': 6, 'D': 1},
    'B': {'A': 6, 'C': 5, 'E': 2},
    'C': {'B': 5, 'E': 5},
    'D': {'A': 1, 'E': 1},
    'E': {'D': 1, 'B': 2, 'C': 5}
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

shortest_distance, shortest_path = dijkstra(graph, 'A', 'C')
print(f"Shortest Path: {shortest_path}, Distance: {shortest_distance}")

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['B', 'E'],
    'D': ['A', 'E'],
    'E': ['D', 'B', 'C']
}

def is_safe(node, color, graph, colors):
    for neighbor in graph[node]:
        if neighbor in colors and colors[neighbor] == color:
            return False
    return True

def graph_coloring(graph, colors, node, available_colors):
    if node is None:
        return True
    
    for color in available_colors:
        if is_safe(node, color, graph, colors):
            colors[node] = color
            next_node = next((n for n in graph if n not in colors), None)
            if graph_coloring(graph, colors, next_node, available_colors):
                return True
            colors.pop(node)
    
    return False

def solve_coloring(graph):
    available_colors = ['Red', 'Green', 'Blue']
    colors = {}
    
    start_node = next(iter(graph))
    if graph_coloring(graph, colors, start_node, available_colors):
        return colors
    return "No valid coloring found"

node_colors = solve_coloring(graph)
print("\nGraph Coloring:", node_colors)

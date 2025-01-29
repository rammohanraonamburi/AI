class Graph:
    def __init__(self):
        self.graph = {
            'a': ['b', 'c'],
            'b': ['f', 'e'],
            'c': ['d', 'e'],
            'd': ['e'],
            'e': ['z'],
            'f': ['z'],
            'z': []  
        }

    def dfs_limited(self, node, depth, path=None, visited=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []

        if depth < 0:
            return  

        visited.add(node)  
        path.append(node)  

        if depth > 0:
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    self.dfs_limited(neighbor, depth - 1, path, visited)

        print(" -> ".join(path))

        path.pop()  

g = Graph()
start_node = 'a'
depth_limit = 2

g.dfs_limited(start_node, depth_limit)

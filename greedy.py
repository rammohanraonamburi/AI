adj_matrix=[[0,3,2,0,0,0,0,0,0,0],
            [0,0,0,4,1,0,0,0,0,0],
            [0,0,0,0,0,3,1,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,5,0,0],
            [0,0,0,0,0,0,0,3,2,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0]]
heuristics=[13,2,4,7,2,8,2,0,4,9]
def greedy(adj_matrix,heuristics,start):
    current=start
    path=[current]
    while heuristics[current]!=0:
        min_h=float('inf')
        next_node=-1
        for neighbor in range(len(adj_matrix[current])):
            if adj_matrix[current][neighbor]>0 and heuristics[neighbor]<min_h:
                min_h=heuristics[neighbor]
                next_node=neighbor
        if next_node==-1:
            return"Goal Node Not Found"
        current=next_node
        path.append(current)
    return f"Goal found at node {current} with path: {path}"
start=0
result=greedy(adj_matrix,heuristics,start)
print(result)

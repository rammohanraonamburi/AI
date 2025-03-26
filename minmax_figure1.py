def minmax_figure1(depth, node_index, is_maximizing, values):
    if depth == 2:
        return values[node_index], [f"C{node_index+1}"]
    
    if is_maximizing:
        best = float('-inf')
        best_path = []
        for i in range(3):
            val, sub_path = minmax_figure1(depth + 1, node_index * 3 + i, False, values)
            if val > best:
                best = val
                best_path = [f"B{i+1}"] + sub_path
        return best, best_path
    else:
        best = float('inf')
        best_path = []
        for i in range(3):
            val, sub_path = minmax_figure1(depth + 1, node_index * 3 + i, True, values)
            if val < best:
                best = val
                best_path = sub_path
        return best, best_path

values_fig1 = [12, 10, 3, 5, 8, 10, 11, 2, 12]
_, optimal_path = minmax_figure1(0, 0, True, values_fig1)
print("Optimal path for Figure 1: A →", " → ".join(optimal_path))

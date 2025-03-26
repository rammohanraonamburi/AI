def minmax_figure2(depth, node_index, is_maximizing, values):
    if depth == 3:
        return values[node_index], [f"Leaf({values[node_index]})"]
    
    if is_maximizing:
        best = float('-inf')
        best_path = []
        for i in range(2):
            val, sub_path = minmax_figure2(depth + 1, node_index * 2 + i, False, values)
            if val > best:
                best = val
                best_path = [f"MAX({best})"] + sub_path
        return best, best_path
    else:
        best = float('inf')
        best_path = []
        for i in range(2):
            val, sub_path = minmax_figure2(depth + 1, node_index * 2 + i, True, values)
            if val < best:
                best = val
                best_path = [f"MIN({best})"] + sub_path
        return best, best_path

values_fig2 = [5, -1, 4, 3, -2, -5, 9, 8, 6, 1, -4, 2, 4, 7, 3, -3]
_, optimal_path_fig2 = minmax_figure2(0, 0, True, values_fig2)
print("Optimal path for Figure 2:", " → ".join(optimal_path_fig2))

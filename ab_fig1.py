def alpha_beta_pruning(node, depth, alpha, beta, is_maximizing, values, path, skipped_nodes):
    if depth == 2:
        return values[node], [node]
    
    if is_maximizing:
        max_value = float('-inf')
        best_path = []
        for child in tree[node]:
            value, child_path = alpha_beta_pruning(child, depth + 1, alpha, beta, False, values, path, skipped_nodes)
            if value > max_value:
                max_value = value
                best_path = [node] + child_path
            alpha = max(alpha, max_value)
            if beta <= alpha:
                skipped_nodes.append(child)
                break
        return max_value, best_path
    else:
        min_value = float('inf')
        best_path = []
        for child in tree[node]:
            value, child_path = alpha_beta_pruning(child, depth + 1, alpha, beta, True, values, path, skipped_nodes)
            if value < min_value:
                min_value = value
                best_path = [node] + child_path
            beta = min(beta, min_value)
            if beta <= alpha:
                skipped_nodes.append(child)
                break
        return min_value, best_path

tree = {
    'A': ['B1', 'B2', 'B3'],
    'B1': ['C1', 'C2', 'C3'],
    'B2': ['C4', 'C5', 'C6'],
    'B3': ['C7', 'C8', 'C9']
}

values = {
    'C1': 12, 'C2': 10, 'C3': 3,
    'C4': 5, 'C5': 8, 'C6': 10,
    'C7': 11, 'C8': 2, 'C9': 12
}

skipped_nodes = []
optimal_value, optimal_path = alpha_beta_pruning('A', 0, float('-inf'), float('inf'), True, values, [], skipped_nodes)
print("Optimal Path:", ' -> '.join(optimal_path))
print("Optimal Value:", optimal_value)
print("Pruned Nodes:", ', '.join(skipped_nodes) if skipped_nodes else "None")
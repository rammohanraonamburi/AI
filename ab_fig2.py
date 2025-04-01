def alpha_beta_search(node, depth, alpha, beta, is_max_turn, node_values, chosen_path, skipped_nodes):
    if depth == 4:
        return node_values[node], [node]
    
    if is_max_turn:
        best_score = float('-inf')
        optimal_route = []
        for child in game_tree[node]:
            score, path = alpha_beta_search(child, depth + 1, alpha, beta, False, node_values, chosen_path, skipped_nodes)
            if score > best_score:
                best_score = score
                optimal_route = [node] + path
            alpha = max(alpha, best_score)
            if beta <= alpha:
                skipped_nodes.append(child)
                break
        return best_score, optimal_route
    else:
        best_score = float('inf')
        optimal_route = []
        for child in game_tree[node]:
            score, path = alpha_beta_search(child, depth + 1, alpha, beta, True, node_values, chosen_path, skipped_nodes)
            if score < best_score:
                best_score = score
                optimal_route = [node] + path
            beta = min(beta, best_score)
            if beta <= alpha:
                skipped_nodes.append(child)
                break
        return best_score, optimal_route

game_tree = {
    'A': ['B1', 'B2'],
    'B1': ['C1', 'C2'],
    'B2': ['C3', 'C4'],
    'C1': ['D1', 'D2'],
    'C2': ['D3', 'D4'],
    'C3': ['D5', 'D6'],
    'C4': ['D7', 'D8'],
    'D1': ['E1', 'E2'],
    'D2': ['E3', 'E4'],
    'D3': ['E5', 'E6'],
    'D4': ['E7', 'E8'],
    'D5': ['E9', 'E10'],
    'D6': ['E11', 'E12'],
    'D7': ['E13', 'E14'],
    'D8': ['E15', 'E16'],
}

node_values = {
    'E1': 5, 'E2': -1, 'E3': 4,
    'E4': 3, 'E5': -2, 'E6': -5,
    'E7': 9, 'E8': 9, 'E9': 6,
    'E10': 1, 'E11': -4, 'E12': 2,
    'E13': 4, 'E14': 7, 'E15': 3, 'E16': -3
}

skipped_nodes = []
best_value, best_path = alpha_beta_search('A', 0, float('-inf'), float('inf'), True, node_values, [], skipped_nodes)
print("Optimal Path:", ' -> '.join(best_path))
print("Optimal Value:", best_value)
print("Pruned Nodes:", ', '.join(skipped_nodes) if skipped_nodes else "None")

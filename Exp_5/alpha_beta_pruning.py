import math

# Leaf values from your image (left to right)
leaves = [10, 21, 9, 15, 14, 18, 22, 9, 5, 2, 4, 1, 3, 18, 23, 5]

def alpha_beta(depth, index, is_max, alpha, beta):
    # Base case: Leaf node reached
    if depth == 4:
        return leaves[index]

    if is_max:
        best = -math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                print(f"Pruning at MAX level (depth {depth})")
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = alpha_beta(depth + 1, index * 2 + i, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                print(f"Pruning at MIN level (depth {depth})")
                break
        return best

# Run the experiment
result = alpha_beta(0, 0, True, -math.inf, math.inf)
print(f"\nThe optimal value is: {result}")
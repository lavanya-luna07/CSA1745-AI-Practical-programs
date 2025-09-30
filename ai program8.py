import math
def minimax(depth, nodeIndex, maximizingPlayer, values, maxDepth):
    if depth == maxDepth:
        return values[nodeIndex]
    if maximizingPlayer:
        best = -math.inf
        for i in range(2):
            val = minimax(depth+1, nodeIndex*2+i, False, values, maxDepth)
            best = max(best, val)
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minimax(depth+1, nodeIndex*2+i, True, values, maxDepth)
            best = min(best, val)
        return best

# New set of leaf values
values = [7, 4, 5, 6, 8, 9, -2, 1]
print("Optimal value:", minimax(0, 0, True, values, 3))

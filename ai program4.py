import heapq
def uniform_cost_search(graph, start, goal):
    # Priority queue: (cost, node, path)
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node in visited:
            continue
        visited.add(node)

        # Goal check
        if node == goal:
            return cost, path

        # Explore neighbors
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))

    return float("inf"), []  # No path found


# Example graph as adjacency list with costs
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Run UCS
cost, path = uniform_cost_search(graph, 'A', 'G')
print("Minimum cost:", cost)
print("Path:", path)

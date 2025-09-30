from collections import deque

def bfs(graph, start):
    visited = set()
    q = deque([start])
    order = []
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            q.extend(graph[node])
    return order

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(bfs(graph, 'A'))

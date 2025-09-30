from heapq import heappush, heappop
def astar(start, goal, graph, h):
    open_set = []
    heappush(open_set, (h(start), 0, start, [start]))
    closed = set()
    while open_set:
        f, g, node, path = heappop(open_set)
        if node == goal:
            return path
        if node in closed:
            continue
        closed.add(node)
        for neigh, cost in graph[node]:
            if neigh not in closed:
                new_g = g + cost
                new_f = new_g + h(neigh)
                heappush(open_set, (new_f, new_g, neigh, path + [neigh]))
    return None

graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',1),('E',5)],
    'C':[('F',2)],
    'D':[('G',3)],
    'E':[('G',1)],
    'F':[('G',6)],
    'G':[]
}

h = lambda n: {'A':7,'B':6,'C':2,'D':2,'E':1,'F':4,'G':0}[n]

print(astar('A','G',graph,h))

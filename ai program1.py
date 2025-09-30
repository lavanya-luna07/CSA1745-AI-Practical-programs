from collections import deque

def is_solvable(puzzle):
    flat = [num for row in puzzle for num in row if num != 0]
    inv = 0
    for i in range(len(flat)):
        for j in range(i+1, len(flat)):
            if flat[i] > flat[j]:
                inv += 1
    return inv % 2 == 0

def puzzle_to_str(puzzle):
    return ''.join(str(num) for row in puzzle for num in row)

def str_to_puzzle(s):
    return [[int(s[3*i+j]) for j in range(3)] for i in range(3)]

def get_neighbors(state):
    i = state.index('0')
    x, y = divmod(i, 3)
    moves = []
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for dx,dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            ni = nx*3+ny
            s = list(state)
            s[i], s[ni] = s[ni], s[i]
            moves.append(''.join(s))
    return moves

def solve(puzzle):
    start = puzzle_to_str(puzzle)
    goal = '123456780'
    if start == goal: return [start]
    if not is_solvable(puzzle): return None
    q = deque([[start]])
    visited = {start}
    while q:
        path = q.popleft()
        for nei in get_neighbors(path[-1]):
            if nei not in visited:
                new_path = path+[nei]
                if nei == goal:
                    return new_path
                q.append(new_path)
                visited.add(nei)
    return None

def print_path(path):
    for s in path:
        p = str_to_puzzle(s)
        for row in p:
            print(row)
        print()

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

solution = solve(start)
if solution:
    print_path(solution)
else:
    print("No solution")

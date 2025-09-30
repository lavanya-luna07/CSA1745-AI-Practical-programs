def print_board(board):
    """Print the chessboard with Q for queen and . for empty."""
    for row in board:
        print(" ".join(row))
    print("\n")
def is_safe(board, row, col, n):
    """Check if placing a queen at (row, col) is safe."""
    for i in range(row):
        if board[i][col] == "Q":
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True

def solve(board, row, n, solutions):
    """Backtracking to place queens row by row."""
    if row == n:  
        solutions.append(["".join(r) for r in board])
        print_board(board) 
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "1"  
            solve(board, row + 1, n, solutions)
            board[row][col] = "0"  

def eight_queens(n=8):
    board = [["." for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(board, 0, n, solutions)
    print(f"Total solutions for {n}-Queens: {len(solutions)}")

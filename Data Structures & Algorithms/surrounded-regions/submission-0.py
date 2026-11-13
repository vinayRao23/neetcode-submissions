class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        queue = collections.deque()
        
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and board[r][c] == "O":
                    queue.append((r, c))
                    board[r][c] = "T"
        
        while queue:
            r, c = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                if r+dr in range(rows) and c+dc in range(cols) and board[r+dr][c+dc] == "O":
                    board[r+dr][c+dc] = "T"
                    queue.append((r+dr, c+dc))
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"

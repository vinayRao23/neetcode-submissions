from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == 2147483647:
                    grid[r+dr][c+dc] = grid[r][c] + 1
                    queue.append((r+dr, c+dc))
                

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        time = 0
        fresh_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        if fresh_count == 0:
            return 0

        while queue and fresh_count > 0:
            queueLen = len(queue)
            for _ in range(queueLen):
                r, c = queue.popleft()
                for dr, dc in directions:
                    if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == 1:
                        grid[r+dr][c+dc] = 2
                        fresh_count -= 1
                        queue.append((r+dr, c+dc))
            time += 1
        
        if fresh_count > 0:
            return -1

        return time
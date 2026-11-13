class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        seen = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            stack = []
            seen.add((r, c))
            stack.append((r, c))
            area = 0

            while stack:
                r, c = stack.pop()
                area += 1
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    if r+dr in range(rows) and c+dc in range(cols) and grid[r+dr][c+dc] == 1 and (r+dr, c+dc) not in seen:
                        seen.add((r+dr, c+dc))
                        stack.append((r+dr, c+dc))
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in seen:
                    max_area = max(dfs(r, c), max_area)
        
        return max_area


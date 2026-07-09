from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        def out_of_bounds(r, c):
            return r < 0 or c < 0 or r >= rows or c >= cols

        size = defaultdict(int)

        def dfs(r, c, label):
            if out_of_bounds(r, c) or grid[r][c] != 1: # visited condition
                return 0
            grid[r][c] = label # modify to prevent repeated visits
            cells = 1
            for dr, dc in [(-1,0),(1,0),(0,1),(0,-1)]:
                cells += dfs(r+dr, c+dc, label)
            return cells
        
        # pre-compute
        label = 2
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    size[label] = dfs(i, j, label)
                    label += 1

        def connect(i, j):
            adjacents = set()
            for di, dj in [(-1,0),(1,0),(0,1),(0,-1)]:
                if out_of_bounds(i+di, j+dj):
                    continue
                adjacents.add(grid[i+di][j+dj])
            total_size = 0
            for label in adjacents:
                total_size += size[label]
            return total_size

        # calculate maximum
        maximum = 0 if not size else max(size.values()) # the current maximum island without any flipping
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0: # try setting
                    maximum = max(maximum, 1 + connect(i, j))
        return maximum
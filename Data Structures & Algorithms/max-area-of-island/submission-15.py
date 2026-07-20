class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        def dfs(r,c,count):
            count = 0
            directions =  [[-1,0],[0,-1],[1,0],[0,1]]
            if r<0 or c<0 or r>=rows or c>=cols:
                return 0
            if grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                count = 1
                grid[r][c] = 0
                for rr,rc in directions:
                    count += dfs(r+rr,c+rc,count)
            return count
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    c = dfs(r,c,0)
                    max_area = max(c,max_area)
        
        return max_area
        
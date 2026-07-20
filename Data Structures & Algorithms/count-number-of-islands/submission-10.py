class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            if r < 0 or c < 0 or r>=rows or c>= cols:
                return
            if grid[r][c] == '0':
                return
            if grid[r][c] == '1':
                grid[r][c] ='0'
                for dr,dc in directions:
                    dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1
        
        return count

            


        
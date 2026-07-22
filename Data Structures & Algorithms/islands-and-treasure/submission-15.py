class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        def bfs(queue):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            while queue:
                len_q = len(queue)
                for _ in range(len_q):
                    r,c = queue.pop(0) 
                    for dr,dc in directions:
                        if r+dr<0 or c+dc<0 or r+dr>=rows or c+dc>=cols:
                            continue
                        if grid[r+dr][c+dc] != 2147483647:
                            continue
                        if grid[r+dr][c+dc] == 2147483647:
                            grid[r+dr][c+dc] = grid[r][c] + 1
                            queue.append([r+dr,c+dc])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append([r,c])

        bfs(queue)  
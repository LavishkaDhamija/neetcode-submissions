class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh+=1
                if grid[r][c] == 2:
                    queue.append([r,c])
        
        def bfs(queue):
            nonlocal fresh
            directions = [[-1,0],[0,-1],[1,0],[0,1]]
            time = 0
            while queue:
                size = len(queue)
                for _ in range(size):
                    rr,cc = queue.pop(0)
                    for dr,dc in directions:
                        if rr+dr<0 or cc+dc<0 or rr+dr>=rows or cc+dc>=cols:
                            continue
                        if grid[rr+dr][cc+dc] == 0:
                            continue 
                        if grid[rr+dr][cc+dc] == 1:
                            fresh -= 1
                            grid[rr+dr][cc+dc] = 2
                            queue.append([rr+dr,cc+dc])
                if queue:                            
                    time += 1
            return time
        

        ans = bfs(queue)
        if fresh > 0:
            return -1
        return ans
    





class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def dfs(r,c):
            directions = [[1,0],[0,1],[-1,0],[0,-1]]
            if r<0 or c<0 or r>=rows or c>=cols:
                return
            if board[r][c] == "X":
                return  
            if board[r][c] == "#":
                return
            if board[r][c] == "O":
                board[r][c] = "#"
            for dr,dc in directions:
                dfs(r+dr,c+dc)
        
        
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and r==0) or (board[r][c] == "O" and c==0) or (board[r][c] == "O" and r==(rows-1)) or (board[r][c] == "O" and c==(cols-1)) :
                    dfs(r,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "#":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"
            
            
        

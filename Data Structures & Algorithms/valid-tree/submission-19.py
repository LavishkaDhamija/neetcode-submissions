class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        for i in range(n):
            adj[i] = []
        for i in range(n):
            for j in range(len(edges)):
                if edges[j][0] == i:
                    adj[i].append(edges[j][1])
                    adj[edges[j][1]].append(i)

        visited = []

        def dfs(node,parent):
            nonlocal visited
            if node in visited:
                return False
            visited.append(node)
            parent_copy = node
            for neighbors in adj[node]:
                if neighbors == parent:
                    continue
                if not dfs(neighbors,parent_copy):
                    return False
            return True
            
            
        
        if not dfs(0,parent = -1):
            return False
        return len(visited) == n
                
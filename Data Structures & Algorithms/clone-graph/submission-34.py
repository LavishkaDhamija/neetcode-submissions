"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        def dfs(node):
            nonlocal cloned
            if node in cloned:
                return cloned[node]
            if node == None:
                return
            newNode = Node(node.val)
            cloned[node] = newNode
            for neighbor in node.neighbors:
                nnode = dfs(neighbor)
                (newNode.neighbors).append(nnode) 
            return cloned[node]

        return dfs(node)
        
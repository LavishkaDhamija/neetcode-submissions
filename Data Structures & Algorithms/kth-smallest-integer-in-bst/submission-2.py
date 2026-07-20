# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        if root is None:
            return 0
        def dfs(root):
            nonlocal result
            if root is None:
                return 
            dfs(root.left)
            result.append(root.val)
            dfs(root.right)
        
        dfs(root)
        ans = result[k-1]
        return ans

        
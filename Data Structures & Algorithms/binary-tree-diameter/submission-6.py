# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def find_height(root):
            nonlocal diameter 
            if root is None:
                return 0
            left = find_height(root.left)
            right = find_height(root.right)
            ans = left + right
            if ans > diameter:
                diameter = ans
            return 1 + max(left,right)

        find_height(root)
        return(diameter)
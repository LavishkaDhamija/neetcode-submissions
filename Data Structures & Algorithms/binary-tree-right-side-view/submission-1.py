# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        resultant = []
        if root is None:
            return []
        queue = [root]
        while queue:
            level = []
            level_size = len(queue)
            for i in range(level_size):
                el = queue.pop(0)
                level.append(el.val)
                left = el.left
                right = el.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            resultant.append(level[-1])

        return resultant
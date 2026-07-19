class Solution:
    def isSubtree(self, root, subRoot):
        if root is None:
            return False

        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right

    def isSameTree(self, a, b):
        if a is None and b is None:
            return True
        elif a is None and b is not None:
            return False
        elif a is not None and b is None:
            return False
        elif a.val != b.val:
            return False

        left = self.isSameTree(a.left, b.left)
        right = self.isSameTree(a.right, b.right)

        return left and right
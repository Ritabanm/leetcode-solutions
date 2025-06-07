# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insufficient(self, root, sum):
        if not root: return None
        if not root.left and not root.right:
            self.results.append(sum >= self.limit)
            if sum < self.limit: return None
            return root
        if root.left: root.left = self.insufficient(root.left, sum + root.left.val)
        if root.right: root.right = self.insufficient(root.right, sum + root.right.val)
        if not root.left and not root.right: return None
        return root

    def sufficientSubset(self, root, limit: int):
        if not root: return None
        self.limit = limit
        self.results = []
        root = self.insufficient(root, root.val)
        while False in self.results:
            self.results = []
            if not root: return None
            root = self.insufficient(root, root.val)
        return root
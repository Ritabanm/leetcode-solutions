class Solution:
    def checkTree(self, root):
        return root.val == root.right.val +root.left.val
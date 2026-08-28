class Solution:
    def diameterOfBinaryTree(Self, root):
        diameter = 0
        def longest_path(node):
            if not node:
                return -1
            nonlocal diameter
            leftpath = longest_path(node.left)
            rightpath = longest_path(node.right)
            diameter = max(diameter, leftpath+rightpath+2)
            return max(leftpath, rightpath)+1
        longest_path(root)
        return diameter
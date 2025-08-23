# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        perfect_sizes = []
        def dfs(root):
            nonlocal perfect_sizes
            if root == None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == right and left != -1:
                perfect_sizes.append(left + right + 1)
                return left + right + 1
            else:
                return -1

        dfs(root)
        perfect_sizes.sort(reverse = True)
        if k > len(perfect_sizes):
            return -1
        return perfect_sizes[k - 1]
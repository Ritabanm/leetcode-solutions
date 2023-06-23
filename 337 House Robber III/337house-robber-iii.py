class Solution:
    def rob(self, root:TreeNode)->int:
        def dfs(root):
            if not root:
                return [0,0]
            leftpair = dfs(root.left)
            rightpair = dfs(root.right)
            withRoot = root.val + leftpair[1] + rightpair[1]
            withoutroot = max(leftpair) + max(rightpair)
            return [withRoot, withoutroot]
        return max(dfs(root))

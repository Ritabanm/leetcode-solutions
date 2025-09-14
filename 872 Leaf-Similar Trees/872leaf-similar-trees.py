class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            ans = []
            if not root:
                return []
            if not root.left and not root.right:
                ans.append(root.val)
            ans += dfs(root.left)
            ans += dfs(root.right)
            return ans

        return dfs(root1) == dfs(root2)
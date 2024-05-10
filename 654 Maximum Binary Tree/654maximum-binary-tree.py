class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(num):
            if not num:
                return None
            root = num.index(max(num))
            node  = TreeNode(max(num))
            node.left = dfs(num[0:root])
            node.right = dfs(num[root+1:])
            return node
        return dfs(nums)
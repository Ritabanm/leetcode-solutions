class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root: return 0
        ans = 1
        def dfs(node, cur):
            nonlocal ans
            if not node: return 
            if node.left and node.val + 1 == node.left.val:
                ans = max(ans, cur+1)
                dfs(node.left, cur+1)
            else: dfs(node.left, 1)
            if node.right and node.val + 1 == node.right.val:
                ans = max(ans, cur+1)
                dfs(node.right, cur+1)
            else: dfs(node.right, 1)  
        dfs(root, 1)        
        return ans
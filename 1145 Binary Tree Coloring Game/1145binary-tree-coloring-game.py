class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:

        most = (n+1)//2

        def dfs(node):
            if not node: return False

            if dfs(node.left) or dfs(node.right): return True
            is_x = node.val == x
            
            l = node.left .val if node.left  else 0
            r = node.right.val if node.right else 0

            if is_x and (l >= most or r >= most): return True

            node.val = 1 + l + r

            if is_x: return node.val < most

            return False

        return dfs(root)
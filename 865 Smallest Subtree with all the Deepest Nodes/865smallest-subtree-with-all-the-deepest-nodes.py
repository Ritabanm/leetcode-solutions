class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # Helper function to perform DFS
        def dfs(node):
            if not node:
                return 0, None  # Depth = 0, LCA = None
            
            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)
            
            if left_depth > right_depth:
                return left_depth + 1, left_lca
            elif right_depth > left_depth:
                return right_depth + 1, right_lca
            else:
                # If both depths are the same, current node is the LCA
                return left_depth + 1, node
        
        # Perform DFS on the root
        _, lca = dfs(root)
        return lca

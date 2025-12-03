class Solution:
    def findTarget(self, root, k):
        def find_pair(root, node, val):
            if not root:
                return False
            if root.val==val and root!=node:
                return True
            
            if root.val<val:
                return find_pair(root.right, node, val)
            return find_pair(root.left, node, val)
        
        def dfs(node):
            if not node:
                return False
            
            if find_pair(root, node, k-node.val):
                return True
            
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
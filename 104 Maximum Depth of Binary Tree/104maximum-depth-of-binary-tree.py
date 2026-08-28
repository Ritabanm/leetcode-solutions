class Solution:
    def maxDepth(self,root):
        if root is None:
            return 0
        
        l_height = self.maxDepth(root.left)
        r_height = self.maxDepth(root.right)
        return max(l_height, r_height)+1
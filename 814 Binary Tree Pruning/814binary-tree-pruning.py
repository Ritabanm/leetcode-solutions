# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        

        return root if self.dfs(root) else None
    def dfs(self, node):
        if not node:
            return False
        if not node.left and not node.right:
            return node.val ==1
        l_has_1 = self.dfs(node.left)
        r_has_1 = self.dfs(node.right)


        if l_has_1 and r_has_1:
            return True
        
        elif l_has_1 and not r_has_1:
            node.right = None
            return True
        elif r_has_1 and not l_has_1:
            node.left = None
            return True 
        else:
            if node.val==1:
                node.left = None
                node.right = None
                return True
            else:
                return False
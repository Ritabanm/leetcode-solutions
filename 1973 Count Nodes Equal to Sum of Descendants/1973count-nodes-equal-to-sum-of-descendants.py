# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (0,0) #(count,sum)
            l,r = dfs(root.left), dfs(root.right)
            if l[1]+r[1] == root.val:
                return (1+l[0]+r[0],l[1]+r[1]+root.val)
            else:
                return (l[0]+r[0],l[1]+r[1]+root.val)
        return dfs(root)[0]
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        #Base Case:
        if root is None:
            return None
        
        #1.Visit left children
        root.left = self.removeLeafNodes(root.left, target)

        #2.Visit right children
        root.right = self.removeLeafNodes(root.right, target)

        #3.Check if current node is leaf & equals target.
        if root.left is None and root.right is None and root.val == target:
            return None
        
        #Untouched otherwise.
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) -> bool:
        if root is None or not arr:
            return False
        if root.val!=arr[0]:
            return False
        if len(arr)==1:
            return root.left is None and root.right is None
        
        return (self.isValidSequence(root.left, arr[1:])or 
    self.isValidSequence(root.right, arr[1:]))
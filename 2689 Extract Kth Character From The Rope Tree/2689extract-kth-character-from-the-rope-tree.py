# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        if root.len ==0:
            return root.val[k-1]
        
        l = (root.left.len if root.left.len else len(root.left.val)) if root.left else 0
        return self.getKthCharacter(root.left, k) if l>=k else self.getKthCharacter(root.right, k-l)
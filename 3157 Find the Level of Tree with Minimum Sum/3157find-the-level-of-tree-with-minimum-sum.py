# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        highest = [1, root.val]

        level = 1
        current = [root]
        while current:
            temp = []
            total = 0
            for x in current:
                total += x.val
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            if highest[1] > total:
                highest = [level, total]
            current = temp
            level += 1

        return highest[0]
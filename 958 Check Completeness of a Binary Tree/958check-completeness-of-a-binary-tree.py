# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        q = deque([root])
        null_node = False
        while q:
            node = q.popleft()
            if node is None:
                null_node = True
            else:
                if null_node:
                    return False
                q.append(node.left)
                q.append(node.right)
        return True
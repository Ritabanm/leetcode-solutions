# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
      
        if root is None:
            return result
        queue = []    
        queue.append(root)
        while queue:
            currentLevelSize = len(queue)
            currentLevelMax = float('-inf')
            for _ in range(currentLevelSize):
                currentNode = queue.pop(0)
                currentLevelMax = max(currentLevelMax, currentNode.val)

                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            result.append(currentLevelMax)
        return result
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        closest = root.val  # Initialize closest with root's value
        
        while root:
            # Update closest if current node's value is closer to target
            # In case of tie (equal difference), prefer the smaller value
            if abs(root.val - target) < abs(closest - target) or (
                abs(root.val - target) == abs(closest - target) and root.val < closest):
                closest = root.val
            
            # Traverse the tree
            if target < root.val:
                root = root.left  # Move to left subtree if target is smaller
            else:
                root = root.right  # Move to right subtree if target is larger
        
        return closest

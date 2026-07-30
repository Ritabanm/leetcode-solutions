class Solution:
    def isValidBST(self,root):
        def validate(node, low = -math.inf, high = math.inf):
            if not node:
                return True
            if node.val<=low or node.val>=high:
                return False
            return validate(node.right, node.val, high) and validate(node.left, low, node.val)
        return validate(root)
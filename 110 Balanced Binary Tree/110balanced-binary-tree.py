class Solution:
    def isBalancedHelper(self, root):
        if not root:
            return True,-1

        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False,0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False,0
        return (abs(leftHeight-rightHeight)<2),1+max(
            leftHeight,rightHeight
        )  
    def isBalanced(self,root):
        return self.isBalancedHelper(root)[0]
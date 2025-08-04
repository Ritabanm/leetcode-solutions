class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def helper(grandparent, parent, node):
            if not node:return
            if grandparent and grandparent.val%2 == 0:self.ans += node.val
            helper(parent, node, node.left)
            helper(parent, node, node.right)
        
        self.ans = 0
        helper(None, None, root)
        return self.ans
class Solution:
    def lowestCommonAncestor(self,root,p,q):
        pval = p.val
        qval = q.val
        node = root
        while node:
            parent_val = node.val
            if pval>parent_val and qval>parent_val:
                node = node.right
            elif pval<parent_val and qval<parent_val:
                node = node.left
            else:
                return node

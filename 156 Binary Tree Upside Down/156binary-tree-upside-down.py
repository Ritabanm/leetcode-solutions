class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        l,r, root.left, root.right = root.left, root.right, None, None
        while l:
            l.left, l.right, root, l, r = r, root, l, l.left, l.right
        
        return root
        
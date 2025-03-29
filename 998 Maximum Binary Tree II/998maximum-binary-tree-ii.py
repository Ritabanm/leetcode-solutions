class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
	
		# dissemble tree A
        def dissemble(node):
            return dissemble(node.left) + [node.val] + dissemble(node.right) if node else []
        
		# construct tree B with val appended. This part is similar to previous question.
        def construct(L):
            if not L: return None
            max_val = max(L)
            max_index = L.index(max_val)
            root = TreeNode(max_val)
            root.left = construct(L[: max_index])
            root.right = construct(L[max_index + 1 :])
            return root

        return construct(dissemble(root) + [val])
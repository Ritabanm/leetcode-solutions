# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.ans = 0

        # return value of dfs = (value of node, length of longest univalue path)
        def dfs(node):
            if not node:
                return (float("-inf"), 0)

            # leaf node
            if not node.left and not node.right:
                return(node.val, 0)

            left_val, left_longest = dfs(node.left)
            right_val, right_longest = dfs(node.right)

            # we have 4 cases
            # case 1 - if both children and the parent node's value is same
            if left_val == right_val == node.val:
                self.ans = max(self.ans, 2 + left_longest + right_longest) # 2 is
                # basically the edge that is joining the left child, right child
                # and the parent of both
                
                # to proceed up the tree, we have to choose one side as if we choose like
                # a triangle of parent, left child, right child, we cannot proceed up
                return (node.val, 1 + max(left_longest, right_longest))
            
            # case 2 - if left child and parent node's value is same
            elif left_val == node.val:
                self.ans = max(self.ans, 1 + left_longest)
                return (node.val, 1 + left_longest)

            # case 3 - if right child and parent node's value is same
            elif right_val == node.val:
                self.ans = max(self.ans, 1 + right_longest)
                return (node.val, 1 + right_longest)

            # case 4 - no matching value so no path yet
            else:
                return (node.val, 0)

        dfs(root)

        return self.ans

# TC
# O(n) where n is number of nodes

# SC
# O(n)